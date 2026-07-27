def build_chat():
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no">
    <title>💎 MNAENCA | دردشة</title>
    <!-- Firebase SDK v10.12.2 -->
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">
    <style>
        {COMMON_CSS}
        body{{height:100vh;height:100dvh;display:flex;flex-direction:column;background:#05140b;overflow:hidden}}
        .header{{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);background:rgba(5,20,11,0.9);backdrop-filter:blur(20px);flex-shrink:0;z-index:10}}
        .btn-back{{background:rgba(16,185,129,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;text-decoration:none;flex-shrink:0}}
        .header-title{{flex:1;min-width:0}}
        .header h2{{font-size:16px;font-weight:700}}
        .header h2 i{{color:var(--accent);margin-left:6px}}
        .conv-list{{flex:1;overflow-y:auto;padding:8px 0}}
        .conv-item{{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid rgba(16,185,129,0.06);cursor:pointer;transition:background 0.2s;animation:fadeIn 0.3s ease}}
        .conv-item:hover{{background:rgba(16,185,129,0.04)}}
        .chat-avatar{{width:50px;height:50px;border-radius:50%;overflow:hidden;border:2px solid rgba(16,185,129,0.3);flex-shrink:0;background:rgba(16,185,129,0.1)}}
        .chat-avatar img{{width:100%;height:100%;object-fit:cover}}
        .conv-info{{flex:1;min-width:0}}
        .conv-name{{font-weight:600;font-size:15px;margin-bottom:3px;display:flex;align-items:center;gap:6px}}
        .conv-last{{font-size:12px;color:rgba(255,255,255,0.4);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
        .chat-msgs{{flex:1;overflow-y:auto;padding:16px 12px;display:flex;flex-direction:column;gap:10px;background:#030d07}}
        
        .bubble-wrapper{{display:flex;flex-direction:column;max-width:80%;animation:msgIn 0.35s cubic-bezier(0.16,1,0.3,1);position:relative}}
        .bubble-wrapper.sent{{align-self:flex-end}}
        .bubble-wrapper.received{{align-self:flex-start}}
        
        .bubble{{padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;position:relative;line-height:1.5;display:flex;flex-direction:column;gap:4px}}
        @keyframes msgIn{{from{{opacity:0;transform:translateY(12px) scale(0.95)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
        .sent .bubble{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-bottom-right-radius:6px;box-shadow:0 4px 15px rgba(16,185,129,0.2)}}
        .received .bubble{{background:rgba(16,185,129,0.08);color:#fff;border:1px solid rgba(16,185,129,0.12);border-bottom-left-radius:6px}}
        .bubble img{{max-width:240px;width:100%;border-radius:14px;cursor:pointer;margin-top:4px;display:block;border:1px solid rgba(255,255,255,0.1)}}
        .bubble audio{{max-width:240px;width:100%;margin-top:4px;outline:none}}
        
        .bubble-footer{{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:4px;font-size:10px;opacity:0.75}}
        .bubble-actions{{display:flex;align-items:center;gap:6px;opacity:0;transition:opacity 0.2s}}
        .bubble-wrapper:hover .bubble-actions{{opacity:1}}
        .btn-copy-msg{{background:none;border:none;color:#fff;cursor:pointer;font-size:11px;padding:2px 4px;border-radius:4px;transition:background 0.2s}}
        .btn-copy-msg:hover{{background:rgba(255,255,255,0.2)}}
        
        .input-bar{{display:flex;gap:8px;padding:10px 12px;background:rgba(5,20,11,0.95);backdrop-filter:blur(20px);border-top:1px solid rgba(16,185,129,0.2);align-items:center;flex-shrink:0;z-index:10;min-height:60px}}
        .input-bar input{{flex:1;padding:12px 18px;border-radius:30px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.25);color:#fff;font-size:14px;outline:none;transition:all 0.3s;min-width:0}}
        .input-bar input:focus{{border-color:var(--accent);box-shadow:0 0 15px rgba(16,185,129,0.15);background:rgba(16,185,129,0.1)}}
        .input-bar input::placeholder{{color:rgba(255,255,255,0.35)}}
        .btn-icon{{width:42px;height:42px;background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);border-radius:50%;color:#fff;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all 0.3s}}
        .btn-icon:hover{{background:rgba(16,185,129,0.25);border-color:var(--accent)}}
        .btn-icon.recording{{background:#ef4444!important;border-color:#f87171!important;animation:pulse 1s infinite}}
        @keyframes pulse{{0%{{transform:scale(1)}}50%{{transform:scale(1.08)}}100%{{transform:scale(1)}}}}
        
        .btn-send{{width:44px;height:44px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 6px 20px rgba(16,185,129,0.4);transition:all 0.3s}}
        .btn-send:hover{{transform:scale(1.05);box-shadow:0 8px 25px rgba(16,185,129,0.6)}}
        .btn-send:active{{transform:scale(0.95)}}
        
        .empty-state{{text-align:center;padding:50px 20px;color:rgba(255,255,255,0.4)}}
        .empty-state i{{font-size:60px;color:var(--accent);opacity:0.3;margin-bottom:16px;display:block}}
        .empty-state p{{font-size:15px;margin-bottom:6px}}
        .empty-state span{{font-size:12px;opacity:0.5}}
        .chat-header-info{{display:flex;align-items:center;gap:12px;flex:1;min-width:0}}
        .chat-header-avatar{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid rgba(16,185,129,0.3);flex-shrink:0}}
        .chat-header-avatar img{{width:100%;height:100%;object-fit:cover}}
        
        .toast-msg{{position:fixed;bottom:80px;left:50%;transform:translateX(-50%);background:rgba(16,185,129,0.95);color:#fff;padding:8px 18px;border-radius:20px;font-size:13px;backdrop-filter:blur(10px);box-shadow:0 4px 15px rgba(0,0,0,0.3);z-index:100;display:none;animation:fadeIn 0.2s ease}}
        .toast-msg.show{{display:block}}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px">
    <div class="spinner"></div>
    <span style="color:rgba(255,255,255,0.5)">💎 جاري تحميل الدردشة...</span>
</div>

<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header"><a href="index.html" class="btn-back"><i class="fas fa-arrow-right"></i></a><div class="header-title"><h2><i class="fas fa-comments"></i> المحادثات</h2></div></div>
    <div class="conv-list" id="convList"></div>
    <div class="empty-state" id="convEmpty" style="display:none"><i class="fas fa-comment-slash"></i><p>لا توجد محادثات</p><span>ابدأ محادثة من ملف المستخدم</span></div>
</div>

<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header">
        <button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button>
        <div class="chat-header-info">
            <div class="chat-header-avatar" id="chatAvatar"><img src="" alt=""></div>
            <div style="flex:1;min-width:0">
                <div style="font-weight:700;font-size:15px" id="chatName">محادثة</div>
                <div style="font-size:11px;opacity:0.5" id="chatOnline"></div>
            </div>
        </div>
        <button class="btn-icon" onclick="copyChat()" title="نسخ كامل المحادثة"><i class="fas fa-copy"></i></button>
    </div>
    
    <div class="chat-msgs" id="msgsList">
        <div class="empty-state"><i class="fas fa-comments"></i><p>ابدأ المحادثة</p><span>أرسل رسالة للبدء 💎</span></div>
    </div>
    
    <div class="input-bar">
        <button class="btn-icon" onclick="sendImage()" title="إرسال صورة"><i class="fas fa-image"></i></button>
        <button class="btn-icon" id="micBtn" onclick="toggleRecord()" title="تسجيل صوتي"><i class="fas fa-microphone"></i></button>
        <input type="text" id="msgInput" placeholder="اكتب رسالتك هنا..." autocomplete="off" onkeydown="if(event.key==='Enter')sendMsg()">
        <button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button>
    </div>
</div>

<div class="toast-msg" id="toastMsg">✅ تم</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null, allUsers={{}}, chatUserId=null;
    let mediaRecorder=null, audioChunks=[], isRecording=false;

    auth.onAuthStateChanged(async u=>{{
        if(!u){{window.location.href='auth.html';return}}
        currentUser=u;
        const us=await db.ref('users').once('value');
        allUsers=us.val()||{{}};
        document.getElementById('loader').style.display='none';
        const params=new URLSearchParams(window.location.search);
        const targetUid=params.get('uid');
        if(targetUid){{openChat(targetUid)}}else{{showConvs()}}
        setInterval(()=>{{if(currentUser)db.ref('users/'+currentUser.uid+'/lastSeen').set(Date.now())}},60000)
    }});

    function showConvs(){{
        document.getElementById('chatView').style.display='none';
        document.getElementById('convView').style.display='flex';
        chatUserId=null;
        loadConvs();
    }}

    async function loadConvs(){{
        const cl=document.getElementById('convList');
        const ce=document.getElementById('convEmpty');
        cl.innerHTML='';
        const snap=await db.ref('private_messages').once('value');
        const all=snap.val()||{{}};
        const found=new Set();
        Object.keys(all).forEach(cid=>{{
            const[u1,u2]=cid.split('_');
            const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;
            if(other&&!found.has(other)&&allUsers[other])found.add(other)
        }});
        if(!found.size){{ce.style.display='block';return}}else{{ce.style.display='none'}}
        found.forEach(uid=>{{
            const u=allUsers[uid];
            const d=document.createElement('div');
            d.className='conv-item';
            d.innerHTML=`<div class="chat-avatar"><img src="${{u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}}" alt="" onerror="this.src='${{DICEBEAR_URL}}?seed=${{uid}}'"></div><div class="conv-info"><div class="conv-name">@${{u?.username||'مستخدم'}} ${{u?.isVerified?'<span style="color:#a7f3d0;font-size:12px"><i class="fas fa-check-circle"></i></span>':''}}</div><div class="conv-last">اضغط للدخول إلى المحادثة 💬</div></div>`;
            d.onclick=()=>openChat(uid);
            cl.appendChild(d);
        }});
    }}

    async function openChat(uid){{
        chatUserId=uid;
        const u=allUsers[uid];
        document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');
        document.getElementById('chatAvatar').querySelector('img').src=u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid);
        document.getElementById('convView').style.display='none';
        document.getElementById('chatView').style.display='flex';
        const onlineEl=document.getElementById('chatOnline');
        db.ref('presence/'+uid).on('value',s=>{{
            const online=s.val();
            onlineEl.innerHTML=online?'<span style="color:#22c55e">● نشط الآن</span>':'آخر ظهور: '+formatTime(u?.lastSeen)
        }});
        await loadMsgs();
        document.getElementById('msgInput').focus();
    }}

    function getChatId(){{return[currentUser.uid,chatUserId].sort().join('_')}}

    async function loadMsgs(){{
        const ml=document.getElementById('msgsList');
        if(!chatUserId)return;
        const snap=await db.ref('private_messages/'+getChatId()).once('value');
        const ms=snap.val()||{{}};
        const msgsArr=Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp);
        if(!msgsArr.length){{
            ml.innerHTML='<div class="empty-state"><i class="fas fa-comments"></i><p>ابدأ المحادثة</p><span>أرسل رسالة للبدء 💎</span></div>';
            return;
        }}
        ml.innerHTML=msgsArr.map(m=>{{
            const sent=m.senderId===currentUser.uid;
            let content='';
            let rawCopyText='';

            if(m.type==='image'){{
                content=`<img src="${{m.imageUrl}}" onclick="window.open('${{m.imageUrl}}','_blank')" loading="lazy">`;
                rawCopyText=m.imageUrl;
            }} else if(m.type==='audio'){{
                content=`<audio controls src="${{m.audioUrl}}"></audio>`;
                rawCopyText=m.audioUrl;
            }} else {{
                content=escapeHtml(m.text);
                rawCopyText=m.text;
            }}

            const time=new Date(m.timestamp).toLocaleTimeString('ar-SA',{{hour:'2-digit',minute:'2-digit'}});
            return `
            <div class="bubble-wrapper ${{sent?'sent':'received'}}">
                <div class="bubble">
                    ${{content}}
                    <div class="bubble-footer">
                        <span>${{time}}</span>
                        <div class="bubble-actions">
                            <button class="btn-copy-msg" onclick="copySingleMsg('${{encodeURIComponent(rawCopyText)}}')" title="نسخ"><i class="fas fa-copy"></i></button>
                        </div>
                    </div>
                </div>
            </div>`;
        }}).join('');
        setTimeout(()=>{{ml.scrollTop=ml.scrollHeight}},100);
    }}

    async function sendMsg(){{
        const inp=document.getElementById('msgInput');
        const txt=inp.value.trim();
        if(!txt||!chatUserId)return;
        inp.value='';
        await db.ref('private_messages/'+getChatId()).push({{senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()}});
        await loadMsgs();
    }}

    async function sendImage(){{
        if(!chatUserId)return;
        const inp=document.createElement('input');
        inp.type='file';
        inp.accept='image/*';
        inp.onchange=async(e)=>{{
            const file=e.target.files[0];
            if(!file)return;
            showToast('⏳ جاري رفع الصورة...');
            const fd=new FormData();
            fd.append('file',file);
            fd.append('upload_preset',UPLOAD_PRESET);
            try{{
                const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{{method:'POST',body:fd}});
                const data=await res.json();
                if(data.secure_url){{
                    await db.ref('private_messages/'+getChatId()).push({{senderId:currentUser.uid,type:'image',imageUrl:data.secure_url,timestamp:Date.now()}});
                    await loadMsgs();
                    showToast('✅ تم إرسال الصورة');
                }}
            }}catch(e){{showToast('❌ فشل رفع الصورة')}}
        }};
        inp.click();
    }}

    /* --- التسجيل الصوتي --- */
    async function toggleRecord(){{
        if(!chatUserId)return;
        const micBtn=document.getElementById('micBtn');
        if(!isRecording){{
            try{{
                const stream=await navigator.mediaDevices.getUserMedia({{audio:true}});
                mediaRecorder=new MediaRecorder(stream);
                audioChunks=[];
                mediaRecorder.ondataavailable=e=>audioChunks.push(e.data);
                mediaRecorder.onstop=async()=>{{
                    const audioBlob=new Blob(audioChunks,{{type:'audio/webm'}});
                    await uploadAudio(audioBlob);
                    stream.getTracks().forEach(track=>track.stop());
                }};
                mediaRecorder.start();
                isRecording=true;
                micBtn.classList.add('recording');
                micBtn.innerHTML='<i class="fas fa-stop"></i>';
                showToast('🎙️ جاري التسجيل...');
            }}catch(err){{
                showToast('❌ يتعذر الوصول إلى الميكروفون');
            }}
        }}else{{
            mediaRecorder.stop();
            isRecording=false;
            micBtn.classList.remove('recording');
            micBtn.innerHTML='<i class="fas fa-microphone"></i>';
        }}
    }}

    async function uploadAudio(blob){{
        showToast('⏳ جاري رفع التسجيل الصوتي...');
        const fd=new FormData();
        fd.append('file',blob);
        fd.append('upload_preset',UPLOAD_PRESET);
        try{{
            const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload',{{method:'POST',body:fd}});
            const data=await res.json();
            if(data.secure_url){{
                await db.ref('private_messages/'+getChatId()).push({{senderId:currentUser.uid,type:'audio',audioUrl:data.secure_url,timestamp:Date.now()}});
                await loadMsgs();
                showToast('✅ تم إرسال التسجيل الصوتي');
            }}
        }}catch(e){{showToast('❌ فشل رفع التسجيل')}}
    }}

    /* --- النسخ --- */
    async function copySingleMsg(encodedText){{
        const text=decodeURIComponent(encodedText);
        try{{
            await navigator.clipboard.writeText(text);
            showToast('✅ تم نسخ النص');
        }}catch(e){{
            const ta=document.createElement('textarea');
            ta.value=text;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showToast('✅ تم نسخ النص');
        }}
    }}

    async function copyChat(){{
        if(!chatUserId)return;
        const snap=await db.ref('private_messages/'+getChatId()).once('value');
        const msgs=snap.val()||{{}};
        let text='💬 محادثة MNAENCA\\n'+'─'.repeat(30)+'\\n';
        Object.values(msgs).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{{
            const sender=m.senderId===currentUser.uid?'أنت':(allUsers[m.senderId]?.username||'مستخدم');
            const content=m.type==='image'?'[صورة]':m.type==='audio'?'[تسجيل صوتي]':m.text;
            const time=new Date(m.timestamp).toLocaleTimeString('ar-SA');
            text+=`\\n${{sender}} (${{time}}):\\n${{content}}\\n`;
        }});
        await copySingleMsg(encodeURIComponent(text));
    }}

    function showToast(msg){{
        const toast=document.getElementById('toastMsg');
        toast.innerText=msg;
        toast.classList.add('show');
        setTimeout(()=>toast.classList.remove('show'),2500);
    }}

    function formatTime(ts){{
        if(!ts)return'غير معروف';
        const diff=Date.now()-ts;
        const mins=Math.floor(diff/60000);
        const hours=Math.floor(diff/3600000);
        const days=Math.floor(diff/86400000);
        if(mins<1)return'الآن';
        if(mins<60)return'منذ '+mins+' د';
        if(hours<24)return'منذ '+hours+' س';
        if(days<7)return'منذ '+days+' يوم';
        return new Date(ts).toLocaleDateString('ar-SA');
    }}

    function escapeHtml(str){{
        return (str||'').replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#039;");
    }}

    console.log('💎 MNAENCA Chat Modernized & Ready ✨');
</script>
</body>
</html>"""
