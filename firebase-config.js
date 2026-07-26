// 💎 MNAENCA 2026 - Emerald Green Luxury Configuration
// Firebase: muvg-42126 | Cloudinary: trz3ktjf
// ✨ PREMIUM: TikTok Comments + Share System + Watermark + Enhanced Profile + Posts

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
const CLOUD_NAME = "trz3ktjf";
const UPLOAD_PRESET = "s44_kk";
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/auto/upload`;

// 💎 MNAENCA Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #064e3b, #059669, #10b981)",
    "linear-gradient(135deg, #022c22, #047857, #34d399)",
    "linear-gradient(135deg, #065f46, #10b981, #6ee7b7)",
    "linear-gradient(135deg, #064e3b, #14b8a6, #5eead4)",
    "linear-gradient(135deg, #047857, #34d399, #a7f3d0)",
    "linear-gradient(135deg, #0f172a, #064e3b, #10b981)"
];

// 💎 App Info
const APP_NAME = "MNAENCA";
const APP_VERSION = "2026.4";
const PRIMARY_COLOR = "#10b981";
const SECONDARY_COLOR = "#a7f3d0";
const WATERMARK_TEXT = "💎 MNAENCA";
const WATERMARK_URL = "https://res.cloudinary.com/trz3ktjf/image/upload/v1/watermark_mnaenca";

console.log('💎 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #10b981; font-size: 16px; font-weight: bold;');
