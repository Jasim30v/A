// 🟦 SOTWE 2026 - Firebase & Cloudinary Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj

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

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const CLOUD_NAME = "dmqyd0haj";
const UPLOAD_PRESET = "s3_gok";

const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const APP_NAME = "Sotwe";
const APP_VERSION = "2026.1";

console.log('🟦 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #1d9bf0; font-size: 16px; font-weight: bold;');
