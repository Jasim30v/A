// 🟦 NEXUS 2026 - Main Script
// All logic: Posts, Comments, Likes, Retweets, Bookmarks, Quotes, Chat, Stories, Search, Admin

let currentUser = null;
let currentUserData = null;
let allUsers = {};
let allPosts = [];
let selectedMediaFile = null;
let currentChatUserId = null;
let viewingProfileUserId = null;
let currentPostForComments = null;
let mediaRecorder = null;
let audioChunks = [];
let bookmarks = {};
let isAdmin = false;

// ========== DATA LOADING ==========
async function loadUserData() {
    const snap = await firebase.database().ref(`users/${currentUser.uid}`).once('value');
    if (snap.exists()) currentUserData = { uid: currentUser.uid, ...snap.val() };
    if (currentUserData?.bookmarks) bookmarks = currentUserData.bookmarks;
}

firebase.database().ref('users').on('value', (s) => { allUsers = s.val() || {}; });

firebase.database().ref('posts').on('value', (s) => {
    const data = s.val();
    if (!data) { allPosts = []; renderFeed(); return; }
    allPosts = [];
    Object.keys(data).forEach(key => allPosts.push({ id: key, ...data[key] }));
    allPosts.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    renderFeed();
});

// ========== MEDIA UPLOAD ==========
async function uploadMedia(file) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('upload_preset', UPLOAD_PRESET);
    let resourceType = 'image';
    if (file.type.startsWith('video/')) resourceType = 'video';
    else if (file.type.startsWith('audio/')) resourceType = 'raw';
    const url = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/${resourceType}/upload`;
    const response = await fetch(url, { method: 'POST', body: formData });
    const data = await response.json();
    return { url: data.secure_url, type: resourceType === 'raw' ? 'audio' : resourceType };
}

// ========== FEED ==========
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function renderFeed() {
    const container = document.getElementById('feedContainer');
    if (!container) return;
    container.innerHTML = '';
    if (allPosts.length === 0) {
        container.innerHTML = '<div class="loading"><div class="spinner"></div><span>لا توجد منشورات بعد</span></div>';
        return;
    }
    allPosts.forEach(post => {
        const user = allUsers[post.sender] || { name: post.senderName || 'مستخدم', avatarUrl: '' };
        const isLiked = post.likedBy && post.likedBy[currentUser?.uid];
        const isRetweeted = post.retweetedBy && post.retweetedBy[currentUser?.uid];
        const isBookmarked = bookmarks[post.id];
        const commentsCount = post.comments ? Object.keys(post.comments).length : 0;
        const retweetCount = post.retweets ? Object.keys(post.retweets).length : 0;

        let mediaHtml = '';
        if (post.mediaUrl) {
            if (post.mediaType === 'image') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation(); openImageModal('${post.mediaUrl}')"><img src="${post.mediaUrl}" loading="lazy"></div>`;
            } else if (post.mediaType === 'video') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation()"><video controls src="${post.mediaUrl}"></video></div>`;
            } else if (post.mediaType === 'audio') {
                mediaHtml = `<div class="tweet-media" onclick="event.stopPropagation()"><audio controls src="${post.mediaUrl}"></audio></div>`;
            }
        }

        let quoteHtml = '';
        if (post.quotePostId && post.quotePostData) {
            const quoteUser = allUsers[post.quotePostData.sender] || { name: 'مستخدم', avatarUrl: '' };
            quoteHtml = `
                <div class="quote-embed" onclick="event.stopPropagation(); openCommentsModal('${post.quotePostId}')">
                    <div style="display:flex;gap:8px;align-items:center;margin-bottom:6px;">
                        <div class="comment-avatar">${quoteUser.avatarUrl ? `<img src="${quoteUser.avatarUrl}">` : (quoteUser.name?.charAt(0) || 'U')}</div>
                        <span style="font-weight:600;font-size:13px;">${escapeHtml(quoteUser.name)}</span>
                    </div>
                    <div style="font-size:13px;">${escapeHtml(post.quotePostData.text?.substring(0, 100) || '')}</div>
                </div>`;
        }

        const div = document.createElement('div');
        div.className = 'tweet-card';
        div.onclick = () => openCommentsModal(post.id);
        div.innerHTML = `
            <div class="tweet-header">
                <div class="tweet-avatar" onclick="event.stopPropagation(); viewProfile('${post.sender}')">${user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || '👤')}</div>
                <div style="flex:1">
                    <div><span class="tweet-name" onclick="event.stopPropagation(); viewProfile('${post.sender}')">${escapeHtml(user.name)}</span><span class="tweet-username mx-1">@${user.name?.toLowerCase().replace(/\s/g, '')}</span><span class="tweet-time">· ${new Date(post.timestamp).toLocaleString()}</span></div>
                    <div class="tweet-content">${escapeHtml(post.text || '')}</div>
                    ${mediaHtml}
                    ${quoteHtml}
                </div>
            </div>
            <div class="tweet-actions" onclick="event.stopPropagation()">
                <button class="tweet-action" onclick="openCommentsModal('${post.id}')"><i class="far fa-comment"></i> <span>${commentsCount}</span></button>
                <button class="tweet-action ${isRetweeted ? 'active' : ''}" onclick="toggleRetweet('${post.id}', this)"><i class="fas fa-retweet"></i> <span>${retweetCount}</span></button>
                <button class="tweet-action ${isLiked ? 'active' : ''}" onclick="toggleLike('${post.id}', this)"><i class="fas fa-heart"></i> <span>${post.likes || 0}</span></button>
                <button class="tweet-action ${isBookmarked ? 'active' : ''}" onclick="toggleBookmark('${post.id}', this)"><i class="fas fa-bookmark"></i></button>
                <button class="tweet-action" onclick="openQuoteModal('${post.id}')"><i class="fas fa-quote-right"></i></button>
            </div>`;
        container.appendChild(div);
    });
}

// ========== COMPOSE ==========
window.openCompose = function() { document.getElementById('composePanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex'; resetCompose(); };
window.closeCompose = function() { document.getElementById('composePanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

function resetCompose() {
    document.getElementById('postText').value = '';
    document.getElementById('mediaPreview').innerHTML = '';
    document.getElementById('mediaPreview').style.display = 'none';
    selectedMediaFile = null;
    document.getElementById('postImage').value = '';
    document.getElementById('postVideo').value = '';
    document.getElementById('postStatus').innerHTML = '';
}

window.previewMedia = function(input, type) {
    const file = input.files[0];
    if (!file) return;
    selectedMediaFile = file;
    const reader = new FileReader();
    reader.onload = function(e) {
        const mediaPreview = document.getElementById('mediaPreview');
        if (type === 'image') mediaPreview.innerHTML = `<img src="${e.target.result}">`;
        else if (type === 'video') mediaPreview.innerHTML = `<video controls><source src="${e.target.result}"></video>`;
        mediaPreview.style.display = 'block';
    };
    reader.readAsDataURL(file);
};

window.startAudioRecording = async function() {
    const btn = document.getElementById('audioRecordBtn');
    if (mediaRecorder && mediaRecorder.state === 'recording') { mediaRecorder.stop(); btn.innerHTML = '<i class="fas fa-microphone"></i>'; return; }
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        mediaRecorder.ondataavailable = (event) => { audioChunks.push(event.data); };
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
            selectedMediaFile = new File([audioBlob], 'recording.mp3', { type: 'audio/mp3' });
            const audioUrl = URL.createObjectURL(audioBlob);
            document.getElementById('mediaPreview').innerHTML = `<audio controls src="${audioUrl}"></audio>`;
            document.getElementById('mediaPreview').style.display = 'block';
            stream.getTracks().forEach(track => track.stop());
        };
        mediaRecorder.start();
        btn.innerHTML = '<i class="fas fa-stop-circle" style="color:#f91880"></i>';
    } catch (err) { showToast('لا يمكن الوصول إلى الميكروفون'); }
};

window.createPost = async function() {
    const text = document.getElementById('postText')?.value || '';
    if (!text.trim() && !selectedMediaFile) { showToast('اكتب شيئاً أو اختر وسائط'); return; }
    document.getElementById('postStatus').innerHTML = '📤 جاري النشر...';
    let mediaUrl = '', mediaType = 'none';
    if (selectedMediaFile) {
        try { const result = await uploadMedia(selectedMediaFile); mediaUrl = result.url; mediaType = result.type; }
        catch (error) { document.getElementById('postStatus').innerHTML = '❌ فشل رفع الوسائط'; return; }
    }
    try {
        await firebase.database().ref('posts').push({
            text, mediaUrl, mediaType, sender: currentUser.uid, senderName: currentUserData?.name,
            likes: 0, likedBy: {}, retweets: {}, retweetedBy: {}, comments: {}, timestamp: Date.now()
        });
        document.getElementById('postStatus').innerHTML = '✅ تم النشر!';
        setTimeout(() => closeCompose(), 1500);
    } catch (error) { document.getElementById('postStatus').innerHTML = '❌ فشل النشر'; }
};

// ========== POST ACTIONS ==========
window.toggleLike = async function(postId, btn) {
    if (!currentUser) return;
    const postRef = firebase.database().ref(`posts/${postId}`);
    const snap = await postRef.once('value');
    const post = snap.val();
    if (!post) return;
    let likes = post.likes || 0;
    let likedBy = post.likedBy || {};
    if (likedBy[currentUser.uid]) { likes--; delete likedBy[currentUser.uid]; showToast('تم إلغاء الإعجاب'); }
    else { likes++; likedBy[currentUser.uid] = true; addNotification(post.sender, 'like', postId); showToast('❤️ أعجبتك');
        if (btn) { const icon = btn.querySelector('i'); if (icon) icon.classList.add('heart-animation'); setTimeout(() => icon?.classList.remove('heart-animation'), 300); } }
    await postRef.update({ likes, likedBy });
    if (btn) { btn.classList.toggle('active'); const span = btn.querySelector('span'); if (span) span.innerText = likes; }
};

window.toggleRetweet = async function(postId, btn) {
    if (!currentUser) return;
    const postRef = firebase.database().ref(`posts/${postId}`);
    const snap = await postRef.once('value');
    const post = snap.val();
    if (!post) return;
    let retweets = post.retweets || {};
    let retweetedBy = post.retweetedBy || {};
    let retweetCount = Object.keys(retweets).length;
    if (retweetedBy[currentUser.uid]) {
        const keyToDelete = Object.keys(retweets).find(k => retweets[k].userId === currentUser.uid);
        if (keyToDelete) delete retweets[keyToDelete];
        delete retweetedBy[currentUser.uid]; retweetCount--; showToast('تم إلغاء إعادة التغريد');
    } else {
        const newRetweetId = Date.now().toString();
        retweets[newRetweetId] = { userId: currentUser.uid, timestamp: Date.now() };
        retweetedBy[currentUser.uid] = true; retweetCount++;
        addNotification(post.sender, 'retweet', postId); showToast('🔁 تم إعادة التغريد');
    }
    await postRef.update({ retweets, retweetedBy });
    if (btn) { btn.classList.toggle('active'); const span = btn.querySelector('span'); if (span) span.innerText = retweetCount; }
};

window.toggleBookmark = async function(postId, btn) {
    if (!currentUser) return;
    const userRef = firebase.database().ref(`users/${currentUser.uid}/bookmarks/${postId}`);
    const snap = await userRef.once('value');
    if (snap.exists()) { await userRef.set(null); delete bookmarks[postId]; showToast('تمت إزالة من الإشارات المرجعية'); }
    else { await userRef.set(true); bookmarks[postId] = true; showToast('📌 تمت إضافة إلى الإشارات المرجعية'); }
    if (btn) btn.classList.toggle('active');
};

window.openQuoteModal = function(postId) {
    const quoteText = prompt('أضف تعليقك على هذا المنشور:');
    if (quoteText) createQuotePost(postId, quoteText);
};

async function createQuotePost(originalPostId, quoteText) {
    const originalPost = allPosts.find(p => p.id === originalPostId);
    if (!originalPost) return;
    await firebase.database().ref('posts').push({
        text: quoteText, mediaUrl: '', mediaType: 'none', sender: currentUser.uid, senderName: currentUserData?.name,
        quotePostId: originalPostId, quotePostData: { text: originalPost.text, sender: originalPost.sender, senderName: originalPost.senderName, mediaUrl: originalPost.mediaUrl, mediaType: originalPost.mediaType },
        likes: 0, likedBy: {}, retweets: {}, retweetedBy: {}, comments: {}, timestamp: Date.now()
    });
    addNotification(originalPost.sender, 'quote', originalPostId);
    showToast('✅ تم نشر الاقتباس');
}

// ========== COMMENTS ==========
window.openCommentsModal = async function(postId) {
    currentPostForComments = postId;
    const post = allPosts.find(p => p.id === postId);
    if (!post) return;
    const container = document.getElementById('commentsList');
    const comments = post.comments || {};
    container.innerHTML = '';
    const sortedComments = Object.entries(comments).sort((a,b) => b[1].timestamp - a[1].timestamp);
    for (const [commentKey, comment] of sortedComments) {
        const user = allUsers[comment.userId] || { name: comment.username || 'مستخدم', avatarUrl: '' };
        const replies = comment.replies || {};
        const commentDiv = document.createElement('div');
        commentDiv.className = 'comment-item';
        commentDiv.innerHTML = `
            <div class="comment-header">
                <div class="comment-avatar" onclick="viewProfile('${comment.userId}')">${user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || 'U')}</div>
                <div style="flex:1"><div><span class="comment-user" onclick="viewProfile('${comment.userId}')">${escapeHtml(user.name)}</span><span class="comment-time mx-2">· ${new Date(comment.timestamp).toLocaleString()}</span></div>
                <div class="comment-text">${escapeHtml(comment.text)}</div></div>
            </div>
            <div class="reply-list" id="replies-${commentKey}"></div>
            <div><button class="text-[#1d9bf0] text-sm mt-2" onclick="showReplyInput('${commentKey}')"><i class="fas fa-reply"></i> رد</button></div>
            <div id="reply-input-${commentKey}" class="mt-2"></div>`;
        const repliesContainer = commentDiv.querySelector(`#replies-${commentKey}`);
        if (repliesContainer && replies) {
            const sortedReplies = Object.entries(replies).sort((a,b) => a[1].timestamp - b[1].timestamp);
            for (const [replyKey, reply] of sortedReplies) {
                const replyUser = allUsers[reply.userId] || { name: reply.username || 'مستخدم', avatarUrl: '' };
                repliesContainer.innerHTML += `<div class="reply-item"><div class="reply-header"><div class="reply-avatar" onclick="viewProfile('${reply.userId}')">${replyUser.avatarUrl ? `<img src="${replyUser.avatarUrl}">` : (replyUser.name?.charAt(0) || 'U')}</div><div class="reply-user" onclick="viewProfile('${reply.userId}')">${escapeHtml(replyUser.name)}</div><div class="comment-time">${new Date(reply.timestamp).toLocaleTimeString()}</div></div><div class="reply-text">${escapeHtml(reply.text)}</div></div>`;
            }
        }
        container.appendChild(commentDiv);
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center text-gray-500 py-10">لا توجد تعليقات بعد</div>';
    document.getElementById('commentsPanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
};

window.closeComments = function() { document.getElementById('commentsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

window.showReplyInput = function(commentId) {
    const replyDiv = document.getElementById(`reply-input-${commentId}`);
    if (!replyDiv) return;
    if (replyDiv.innerHTML) { replyDiv.innerHTML = ''; return; }
    replyDiv.innerHTML = `<div class="flex gap-2 mt-2"><input type="text" id="reply-text-${commentId}" class="flex-1 bg-[#1a1a1a] border border-[#2f3336] rounded-full px-3 py-2 text-sm" placeholder="اكتب رداً..." onkeypress="if(event.key==='Enter') addReply('${commentId}')"><button onclick="addReply('${commentId}')" class="bg-[#1d9bf0] text-white px-4 py-2 rounded-full text-sm">نشر</button></div>`;
};

window.addReply = async function(commentId) {
    const input = document.getElementById(`reply-text-${commentId}`);
    const text = input?.value;
    if (!text?.trim()) return;
    await firebase.database().ref(`posts/${currentPostForComments}/comments/${commentId}/replies`).push({ userId: currentUser.uid, username: currentUserData?.name, text, timestamp: Date.now() });
    if (input) input.value = '';
    openCommentsModal(currentPostForComments);
};

window.addComment = async function() {
    const input = document.getElementById('commentInput');
    const text = input?.value;
    if (!text?.trim() || !currentPostForComments) return;
    await firebase.database().ref(`posts/${currentPostForComments}/comments`).push({ userId: currentUser.uid, username: currentUserData?.name, text, replies: {}, timestamp: Date.now() });
    if (input) input.value = '';
    openCommentsModal(currentPostForComments);
    const post = allPosts.find(p => p.id === currentPostForComments);
    if (post) addNotification(post.sender, 'comment', currentPostForComments);
};

// ========== NOTIFICATIONS ==========
async function addNotification(targetUserId, type, postId = null) {
    if (targetUserId === currentUser.uid) return;
    const messages = { like: '❤️ أعجب بمنشورك', comment: '💬 علق على منشورك', retweet: '🔁 أعاد تغريد منشورك', quote: '📝 اقتبس منشورك', follow: '👥 بدأ بمتابعتك' };
    await firebase.database().ref(`notifications/${targetUserId}`).push({ type, fromUserId: currentUser.uid, fromUsername: currentUserData?.name, message: messages[type], postId: postId, timestamp: Date.now(), read: false });
    updateNotificationBadge();
}

function updateNotificationBadge() {
    if (!currentUser?.uid) return;
    firebase.database().ref(`notifications/${currentUser.uid}`).on('value', (snap) => {
        const notifs = snap.val() || {};
        const unread = Object.values(notifs).filter(n => !n.read).length;
        const badge = document.getElementById('notifBadge');
        if (badge) {
            if (unread > 0) { badge.style.display = 'flex'; badge.innerText = unread > 9 ? '9+' : unread; }
            else badge.style.display = 'none';
        }
    });
}

window.openNotifications = async function() {
    const panel = document.getElementById('notificationsPanel');
    const snap = await firebase.database().ref(`notifications/${currentUser.uid}`).once('value');
    const notifs = snap.val() || {};
    const container = document.getElementById('notificationsList');
    container.innerHTML = '';
    const sorted = Object.entries(notifs).sort((a,b) => b[1].timestamp - a[1].timestamp);
    for (const [key, n] of sorted) {
        const icons = { like: '❤️', comment: '💬', retweet: '🔁', quote: '📝', follow: '👥' };
        const bgColor = n.read ? '' : 'background:rgba(29,155,240,0.1);border-right:4px solid #1d9bf0;';
        container.innerHTML += `<div class="notification-item" style="${bgColor}" onclick="handleNotificationClick('${n.type}', '${n.fromUserId}', '${n.postId || ''}')"><div class="text-2xl">${icons[n.type] || '🔔'}</div><div class="flex-1"><div class="font-bold">${escapeHtml(n.fromUsername)}</div><div class="text-sm" style="color:#71767b">${n.message}</div><div class="text-xs mt-1" style="color:#71767b">${new Date(n.timestamp).toLocaleString()}</div></div></div>`;
        if (!n.read) await firebase.database().ref(`notifications/${currentUser.uid}/${key}`).update({ read: true });
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد إشعارات</div>';
    panel.classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};

window.handleNotificationClick = function(type, userId, postId) { closeNotifications(); if (type === 'follow') viewProfile(userId); else if (postId) openCommentsModal(postId); };
window.closeNotifications = function() { document.getElementById('notificationsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

// ========== TOAST ==========
function showToast(message) {
    let toast = document.getElementById('customToast');
    if (!toast) { toast = document.createElement('div'); toast.id = 'customToast'; document.body.appendChild(toast); }
    toast.innerText = message; toast.style.opacity = '1';
    setTimeout(() => { toast.style.opacity = '0'; }, 3000);
}

// ========== PROFILE ==========
window.openMyProfile = function() { viewProfile(currentUser.uid); };
window.viewProfile = async function(userId) {
    if (!userId) return;
    viewingProfileUserId = userId;
    await loadProfileData(userId);
    document.getElementById('profilePanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
};
window.closeProfile = function() { document.getElementById('profilePanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

async function loadProfileData(userId) {
    const userSnap = await firebase.database().ref(`users/${userId}`).once('value');
    const user = userSnap.val();
    if (!user) return;
    const coverEl = document.getElementById('profileCover');
    if (user.coverUrl) coverEl.style.background = `url(${user.coverUrl}) center/cover`;
    else coverEl.style.background = 'linear-gradient(135deg, #1d9bf0, #f91880)';
    const avatarEl = document.getElementById('profileAvatar');
    avatarEl.innerHTML = user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.name?.charAt(0) || '👤');
    document.getElementById('profileName').innerText = user.name;
    document.getElementById('profileBio').innerText = user.bio || '✏️ أضف سيرة ذاتية';
    const userPosts = allPosts.filter(p => p.sender === userId);
    document.getElementById('profilePostsCount').innerText = userPosts.length;
    document.getElementById('profileFollowersCount').innerText = Object.keys(user.followers || {}).length;
    document.getElementById('profileFollowingCount').innerText = Object.keys(user.following || {}).length;
    const grid = document.getElementById('profilePostsGrid');
    grid.innerHTML = userPosts.map(post => `<div class="profile-post" onclick="openCommentsModal('${post.id}')">${post.mediaUrl ? (post.mediaType === 'image' ? `<img src="${post.mediaUrl}" loading="lazy">` : post.mediaType === 'video' ? `<video src="${post.mediaUrl}"></video>` : '<i class="fas fa-music text-2xl"></i>') : '<i class="fas fa-file-alt text-2xl"></i>'}</div>`).join('');
    if (userPosts.length === 0) grid.innerHTML = '<div class="col-span-3 text-center py-10" style="color:#71767b">لا توجد منشورات</div>';
    const buttonsDiv = document.getElementById('profileButtons');
    buttonsDiv.innerHTML = '';
    if (userId === currentUser.uid) {
        buttonsDiv.innerHTML = `<button class="profile-btn btn-primary" onclick="openEditProfileModal()">✏️ تعديل الملف</button><button class="profile-btn btn-secondary" onclick="logout()">🚪 تسجيل خروج</button>${isAdmin ? '<button class="profile-btn btn-secondary" onclick="openAdmin()">🔧 لوحة التحكم</button>' : ''}`;
    } else {
        const isFollowing = currentUserData?.following && currentUserData.following[userId];
        buttonsDiv.innerHTML = `<button class="profile-btn btn-primary" onclick="toggleFollow('${userId}', this)">${isFollowing ? '✅ متابع' : '➕ متابعة'}</button><button class="profile-btn btn-secondary" onclick="openPrivateChat('${userId}')"><i class="fas fa-envelope"></i> مراسلة</button>`;
    }
}

window.openEditProfileModal = function() { document.getElementById('editName').value = currentUserData?.name || ''; document.getElementById('editBio').value = currentUserData?.bio || ''; document.getElementById('editProfileModal').classList.add('open'); };
window.closeEditProfileModal = function() { document.getElementById('editProfileModal').classList.remove('open'); };
window.saveProfileEdit = async function() {
    const newName = document.getElementById('editName').value;
    const newBio = document.getElementById('editBio').value;
    if (!newName.trim()) { showToast('الاسم مطلوب'); return; }
    await firebase.database().ref(`users/${currentUser.uid}`).update({ name: newName.trim(), bio: newBio });
    showToast('✅ تم تحديث الملف الشخصي');
    closeEditProfileModal();
    setTimeout(() => location.reload(), 1000);
};

// ========== AVATAR / COVER UPLOAD ==========
window.changeAvatar = function() { document.getElementById('avatarInput')?.click(); };
window.changeCover = function() { document.getElementById('coverInput')?.click(); };

(function setupUploadInputs() {
    if (!document.getElementById('avatarInput')) {
        const inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.id = 'avatarInput'; inp.style.display = 'none';
        document.body.appendChild(inp);
        inp.addEventListener('change', async (e) => {
            const file = e.target.files[0]; if (!file) return;
            showToast('📤 جاري رفع الصورة...');
            const result = await uploadMedia(file);
            await firebase.database().ref(`users/${currentUser.uid}`).update({ avatarUrl: result.url });
            showToast('✅ تم تحديث الصورة الشخصية'); location.reload();
        });
    }
    if (!document.getElementById('coverInput')) {
        const inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.id = 'coverInput'; inp.style.display = 'none';
        document.body.appendChild(inp);
        inp.addEventListener('change', async (e) => {
            const file = e.target.files[0]; if (!file) return;
            showToast('📤 جاري رفع الصورة...');
            const result = await uploadMedia(file);
            await firebase.database().ref(`users/${currentUser.uid}`).update({ coverUrl: result.url });
            showToast('✅ تم تحديث صورة الغلاف'); location.reload();
        });
    }
})();

// ========== FOLLOW ==========
window.toggleFollow = async function(userId, btn) {
    if (!currentUser || currentUser.uid === userId) return;
    const userRef = firebase.database().ref(`users/${currentUser.uid}/following/${userId}`);
    const targetRef = firebase.database().ref(`users/${userId}/followers/${currentUser.uid}`);
    const snap = await userRef.once('value');
    if (snap.exists()) { await userRef.set(null); await targetRef.set(null); if (btn) btn.innerText = '➕ متابعة'; showToast(`👋 توقفت عن متابعة ${allUsers[userId]?.name}`); }
    else { await userRef.set(true); await targetRef.set(true); if (btn) btn.innerText = '✅ متابع'; addNotification(userId, 'follow'); showToast(`👥 بدأت بمتابعة ${allUsers[userId]?.name}`); }
    if (viewingProfileUserId === userId) await loadProfileData(userId);
};

window.openFollowersList = async function(type) {
    document.getElementById('followersTitle').innerText = type === 'followers' ? 'المتابعون' : 'المتابَعون';
    const container = document.getElementById('followersList');
    const user = viewingProfileUserId ? allUsers[viewingProfileUserId] : currentUserData;
    const list = type === 'followers' ? user?.followers : user?.following;
    container.innerHTML = '';
    if (list) {
        for (const [uid] of Object.entries(list)) {
            const u = allUsers[uid];
            if (u) container.innerHTML += `<div class="follower-item" onclick="viewProfile('${uid}')"><div class="avatar-xs">${u.avatarUrl ? `<img src="${u.avatarUrl}">` : (u.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(u.name)}</div><div class="text-sm" style="color:#71767b">@${u.name?.toLowerCase().replace(/\s/g, '')}</div></div></div>`;
        }
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا يوجد مستخدمين</div>';
    document.getElementById('followersPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeFollowers = function() { document.getElementById('followersPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

// ========== CHAT ==========
function getChatId(uid1, uid2) { return uid1 < uid2 ? `${uid1}_${uid2}` : `${uid2}_${uid1}`; }

window.openConversations = async function() {
    const panel = document.getElementById('conversationsPanel');
    const container = document.getElementById('conversationsList');
    const convSnap = await firebase.database().ref(`private_chats/${currentUser.uid}`).once('value');
    const conversations = convSnap.val() || {};
    container.innerHTML = '';
    for (const [otherId, convData] of Object.entries(conversations)) {
        const otherUser = allUsers[otherId];
        if (otherUser) container.innerHTML += `<div class="conversation-item" onclick="openPrivateChat('${otherId}')"><div class="avatar-sm">${otherUser.avatarUrl ? `<img src="${otherUser.avatarUrl}">` : (otherUser.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(otherUser.name)}</div><div class="text-sm" style="color:#71767b">${convData.lastMessage?.substring(0, 40) || 'رسالة'}</div></div></div>`;
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد محادثات بعد</div>';
    panel.classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeConversations = function() { document.getElementById('conversationsPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };

window.openPrivateChat = async function(otherUserId) {
    currentChatUserId = otherUserId;
    const user = allUsers[otherUserId];
    document.getElementById('chatUserName').innerText = user?.name || 'مستخدم';
    document.getElementById('chatAvatar').innerHTML = user?.avatarUrl ? `<img src="${user.avatarUrl}">` : (user?.name?.charAt(0) || 'U');
    await loadPrivateMessages(otherUserId);
    document.getElementById('chatPanel').classList.add('open');
    document.getElementById('backBtn').style.display = 'flex';
    closeConversations();
};
window.closeChat = function() { document.getElementById('chatPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; currentChatUserId = null; };

async function loadPrivateMessages(otherUserId) {
    const container = document.getElementById('chatMessages');
    container.innerHTML = '<div class="text-center py-10" style="color:#71767b">جاري التحميل...</div>';
    const chatId = getChatId(currentUser.uid, otherUserId);
    const messagesSnap = await firebase.database().ref(`private_messages/${chatId}`).once('value');
    const messages = messagesSnap.val() || {};
    container.innerHTML = '';
    const sorted = Object.entries(messages).sort((a,b)=>a[1].timestamp-b[1].timestamp);
    for (const [id, msg] of sorted) {
        const isSent = msg.senderId === currentUser.uid;
        const time = new Date(msg.timestamp).toLocaleTimeString();
        let content = '';
        if (msg.type === 'text') content = `<div class="message-bubble ${isSent ? 'sent' : 'received'}">${escapeHtml(msg.text)}</div>`;
        else if (msg.type === 'image') content = `<img src="${msg.imageUrl}" class="message-image" onclick="openImageModal('${msg.imageUrl}')">`;
        else if (msg.type === 'audio') content = `<div class="message-audio"><audio controls src="${msg.audioUrl}"></audio></div>`;
        container.innerHTML += `<div class="chat-message ${isSent ? 'sent' : 'received'}"><div>${content}<div style="font-size:10px;opacity:0.5;margin-top:4px;">${time}</div></div></div>`;
    }
    if (container.innerHTML === '') container.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد رسائل بعد</div>';
    container.scrollTop = container.scrollHeight;
}

window.sendChatMessage = async function() {
    const input = document.getElementById('chatMessageInput');
    const text = input?.value.trim();
    if (!text || !currentChatUserId) return;
    const chatId = getChatId(currentUser.uid, currentChatUserId);
    await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, text, type: 'text', timestamp: Date.now() });
    await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: text, lastTimestamp: Date.now(), withUser: currentChatUserId });
    await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: text, lastTimestamp: Date.now(), withUser: currentUser.uid });
    input.value = '';
    await loadPrivateMessages(currentChatUserId);
};

window.sendChatImage = async function(input) {
    const file = input.files[0]; if (!file || !currentChatUserId) return;
    const result = await uploadMedia(file);
    const chatId = getChatId(currentUser.uid, currentChatUserId);
    await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, imageUrl: result.url, type: 'image', timestamp: Date.now() });
    await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: '📷 صورة', lastTimestamp: Date.now(), withUser: currentChatUserId });
    await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: '📷 صورة', lastTimestamp: Date.now(), withUser: currentUser.uid });
    input.value = '';
    await loadPrivateMessages(currentChatUserId);
};

window.startRecordingChat = async function() {
    const btn = document.getElementById('chatRecordBtn');
    if (mediaRecorder && mediaRecorder.state === 'recording') { mediaRecorder.stop(); btn.innerHTML = '<i class="fas fa-microphone"></i>'; return; }
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream); audioChunks = [];
        mediaRecorder.ondataavailable = (event) => { audioChunks.push(event.data); };
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
            const audioFile = new File([audioBlob], 'recording.mp3', { type: 'audio/mp3' });
            const result = await uploadMedia(audioFile);
            if (currentChatUserId) {
                const chatId = getChatId(currentUser.uid, currentChatUserId);
                await firebase.database().ref(`private_messages/${chatId}`).push({ senderId: currentUser.uid, senderName: currentUserData?.name, audioUrl: result.url, type: 'audio', timestamp: Date.now() });
                await firebase.database().ref(`private_chats/${currentUser.uid}/${currentChatUserId}`).set({ lastMessage: '🎤 رسالة صوتية', lastTimestamp: Date.now(), withUser: currentChatUserId });
                await firebase.database().ref(`private_chats/${currentChatUserId}/${currentUser.uid}`).set({ lastMessage: '🎤 رسالة صوتية', lastTimestamp: Date.now(), withUser: currentUser.uid });
                await loadPrivateMessages(currentChatUserId);
            }
            stream.getTracks().forEach(track => track.stop());
        };
        mediaRecorder.start();
        btn.innerHTML = '<i class="fas fa-stop-circle" style="color:#f91880"></i>';
    } catch (err) { showToast('لا يمكن الوصول إلى الميكروفون'); }
};

// ========== SEARCH ==========
window.openSearch = function() { document.getElementById('searchPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex'; };
window.closeSearch = function() { document.getElementById('searchPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };
window.searchAll = function() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const resultsDiv = document.getElementById('searchResults');
    if (!query) { resultsDiv.innerHTML = ''; return; }
    const users = Object.values(allUsers).filter(u => u.name?.toLowerCase().includes(query));
    resultsDiv.innerHTML = users.map(u => `<div class="search-result" onclick="viewProfile('${u.uid}')"><div class="avatar-xs">${u.avatarUrl ? `<img src="${u.avatarUrl}">` : (u.name?.charAt(0) || 'U')}</div><div><div class="font-bold">${escapeHtml(u.name)}</div><div class="text-sm" style="color:#71767b">@${u.name?.toLowerCase().replace(/\s/g, '')}</div></div></div>`).join('');
    if (users.length === 0) resultsDiv.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا توجد نتائج</div>';
};

// ========== ADMIN ==========
window.openAdmin = async function() {
    if (!isAdmin) return;
    const totalUsers = Object.keys(allUsers).length;
    const totalPosts = allPosts.length;
    const totalLikes = allPosts.reduce((s,p)=>s+(p.likes||0),0);
    const totalComments = allPosts.reduce((s,p)=>s+(p.comments ? Object.keys(p.comments).length : 0),0);
    document.getElementById('adminStats').innerHTML = `
        <div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-users"></i></div><div class="admin-stat-number">${totalUsers}</div><div class="admin-stat-label">مستخدمين</div></div>
        <div class="admin-stat"><div class="admin-stat-icon"><i class="fas fa-file-alt"></i></div><div class="admin-stat-number">${totalPosts}</div><div class="admin-stat-label">منشورات</div></div>
        <div class="admin-stat"><div class="admin-stat-icon" style="color:#f91880"><i class="fas fa-heart"></i></div><div class="admin-stat-number">${totalLikes}</div><div class="admin-stat-label">إعجابات</div></div>
        <div class="admin-stat"><div class="admin-stat-icon" style="color:#1d9bf0"><i class="fas fa-comment"></i></div><div class="admin-stat-number">${totalComments}</div><div class="admin-stat-label">تعليقات</div></div>`;
    const usersListDiv = document.getElementById('adminUsersList');
    usersListDiv.innerHTML = '';
    Object.entries(allUsers).forEach(([uid, u]) => {
        if (uid !== currentUser.uid) usersListDiv.innerHTML += `<div class="admin-item"><div><div class="admin-item-name">${escapeHtml(u.name)}</div><div class="admin-item-email">${u.email}</div></div><button class="admin-delete-btn" onclick="adminDeleteUser('${uid}')"><i class="fas fa-trash"></i> حذف</button></div>`;
    });
    if (usersListDiv.innerHTML === '') usersListDiv.innerHTML = '<div class="text-center py-10" style="color:#71767b">لا يوجد مستخدمين آخرين</div>';
    const postsListDiv = document.getElementById('adminPostsList');
    postsListDiv.innerHTML = '';
    allPosts.slice(0, 30).forEach(post => {
        postsListDiv.innerHTML += `<div class="admin-item"><div><div class="admin-item-name">${escapeHtml(post.senderName || 'مستخدم')}</div><div class="admin-item-email">${post.text?.substring(0, 60) || 'منشور بدون نص'} · ${new Date(post.timestamp).toLocaleString()}</div></div><button class="admin-delete-btn" onclick="adminDeletePost('${post.id}')"><i class="fas fa-trash"></i> حذف</button></div>`;
    });
    document.getElementById('adminPanel').classList.add('open'); document.getElementById('backBtn').style.display = 'flex';
};
window.closeAdmin = function() { document.getElementById('adminPanel').classList.remove('open'); if (!document.querySelector('.panel.open')) document.getElementById('backBtn').style.display = 'none'; };
window.adminDeleteUser = async function(userId) { if (!isAdmin || !confirm('⚠️ حذف هذا المستخدم وجميع منشوراته؟')) return; const posts = allPosts.filter(p => p.sender === userId); for (const post of posts) await firebase.database().ref(`posts/${post.id}`).set(null); await firebase.database().ref(`users/${userId}`).set(null); showToast('✅ تم حذف المستخدم'); location.reload(); };
window.adminDeletePost = async function(postId) { if (!isAdmin || !confirm('⚠️ حذف هذا المنشور؟')) return; await firebase.database().ref(`posts/${postId}`).set(null); showToast('✅ تم حذف المنشور'); renderFeed(); };

// ========== NAVIGATION ==========
window.switchTab = function(tab) { const navItems = document.querySelectorAll('.nav-item'); navItems.forEach(t => t.classList.remove('active')); if (event && event.target) { const clicked = event.target.closest('.nav-item'); if (clicked) clicked.classList.add('active'); } if (tab === 'home') { closeCompose(); closeProfile(); closeChat(); closeConversations(); closeNotifications(); closeSearch(); closeComments(); closeFollowers(); closeAdmin(); closeEditProfileModal(); } };
window.goToHome = function() { const homeBtn = document.querySelector('.nav-item i.fa-home')?.closest('.nav-item'); if (homeBtn) { document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active')); homeBtn.classList.add('active'); } closeCompose(); closeProfile(); closeChat(); closeConversations(); closeNotifications(); closeSearch(); closeComments(); closeFollowers(); closeAdmin(); closeEditProfileModal(); document.getElementById('backBtn').style.display = 'none'; };
window.goBack = function() {
    if (document.getElementById('commentsPanel')?.classList.contains('open')) closeComments();
    else if (document.getElementById('profilePanel')?.classList.contains('open')) closeProfile();
    else if (document.getElementById('chatPanel')?.classList.contains('open')) closeChat();
    else if (document.getElementById('conversationsPanel')?.classList.contains('open')) closeConversations();
    else if (document.getElementById('notificationsPanel')?.classList.contains('open')) closeNotifications();
    else if (document.getElementById('searchPanel')?.classList.contains('open')) closeSearch();
    else if (document.getElementById('followersPanel')?.classList.contains('open')) closeFollowers();
    else if (document.getElementById('adminPanel')?.classList.contains('open')) closeAdmin();
    else if (document.getElementById('composePanel')?.classList.contains('open')) closeCompose();
    else if (document.getElementById('editProfileModal')?.classList.contains('open')) closeEditProfileModal();
    else goToHome();
};
window.logout = function() { firebase.auth().signOut(); location.reload(); };

// ========== AUTH STATE ==========
firebase.auth().onAuthStateChanged(async (user) => {
    if (user) {
        currentUser = user;
        await loadUserData();
        isAdmin = ADMIN_EMAILS.includes(currentUser.email);
        document.getElementById('mainApp').style.display = 'block';
        updateNotificationBadge();
        if (localStorage.getItem('theme') === 'light') document.body.classList.add('light-mode');
        showToast(`👋 مرحباً ${currentUserData?.name || 'مستخدم'}`);
    } else {
        window.location.replace('auth.html');
    }
});

console.log('🟦 Nexus Platform Ready ✨');
