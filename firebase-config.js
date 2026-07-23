// 🌑 MNAENCA 2026 - Dark Purple Luxury Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj
// ✨ PREMIUM: TikTok Comments + Share System + Watermark + Enhanced Profile

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

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

// Cloudinary Configuration
const CLOUD_NAME = "dmqyd0haj";
const UPLOAD_PRESET = "s3_gok";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/auto/upload`;

// 🌑 MNAENCA Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #1a0020, #2d0040, #4a0060)",
    "linear-gradient(135deg, #0d0033, #1a0050, #2d0070)",
    "linear-gradient(135deg, #1a0030, #2d0050, #4a0070)",
    "linear-gradient(135deg, #200030, #3d0060, #5a0090)",
    "linear-gradient(135deg, #150025, #280045, #400065)",
    "linear-gradient(135deg, #0a0a1a, #1a1040, #2d1a60)"
];

// 🌑 App Info
const APP_NAME = "MNAENCA";
const APP_VERSION = "2026.4";
const PRIMARY_COLOR = "#a855f7";
const SECONDARY_COLOR = "#ec4899";
const WATERMARK_TEXT = "🌑 MNAENCA";
const WATERMARK_URL = "https://res.cloudinary.com/dmqyd0haj/image/upload/v1/watermark_mnaenca";

console.log('%c🌑 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #a855f7; font-size: 16px; font-weight: bold;');
