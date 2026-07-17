// 🟦 NEXUS 2026 - Firebase & Cloudinary Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj
// ✨ PREMIUM: Notifications + Likes + Retweets + Chat + Stories + Admin

// 🔥 Firebase Configuration
const firebaseConfig = {
    apiKey: "AIzaSyCqDvG98pEqmZHKZienquJEq6gS1kNjK8M",
    authDomain: "muvg-42126.firebaseapp.com",
    databaseURL: "https://muvg-42126-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "muvg-42126",
    storageBucket: "muvg-42126.firebasestorage.app",
    messagingSenderId: "514075097173",
    appId: "1:514075097173:web:6fab4e9598549691cc7cdc",
    measurementId: "G-4VP8E6WJ48"
};

// Initialize Firebase (Compat)
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Database reference helpers
const ref = (path) => firebase.database().ref(path);
const push = (ref) => ref.push();
const set = (ref, data) => ref.set(data);
const update = (ref, data) => ref.update(data);
const get = (ref) => ref.once('value');
const child = (ref, path) => ref.child(path);
const remove = (ref) => ref.remove();
const onValue = (ref, callback) => ref.on('value', callback);

// ☁️ Cloudinary Configuration
const CLOUD_NAME = "dmqyd0haj";
const UPLOAD_PRESET = "s3_gok";

// 🟦 NEXUS Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const APP_NAME = "Nexus";
const APP_VERSION = "2026.1";
const PRIMARY_COLOR = "#1d9bf0";
const SECONDARY_COLOR = "#f91880";

console.log('🟦 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #1d9bf0; font-size: 16px; font-weight: bold;');
