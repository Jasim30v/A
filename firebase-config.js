// 💖 MNAENCA 2026 - Rose Pink Luxury Configuration
// Firebase: muvg-42126 | Cloudinary: trz3ktjf
// ✨ PREMIUM: TikTok Comments + Share System + Watermark + Enhanced Profile + Voice + Image

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

// 💖 MNAENCA Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #831843, #be185d, #ec4899)",
    "linear-gradient(135deg, #4c0519, #9d174d, #db2777)",
    "linear-gradient(135deg, #701a75, #a21caf, #d946ef)",
    "linear-gradient(135deg, #831843, #e11d48, #fb7185)",
    "linear-gradient(135deg, #9d174d, #f43f5e, #fda4af)",
    "linear-gradient(135deg, #1a1a2e, #9d174d, #ec4899)"
];

// 💖 App Info
const APP_NAME = "MNAENCA";
const APP_VERSION = "2026.3";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#fbcfe8";
const WATERMARK_TEXT = "💖 MNAENCA";
const WATERMARK_URL = "https://res.cloudinary.com/trz3ktjf/image/upload/v1/watermark_mnaenca";

console.log('💖 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 16px; font-weight: bold;');
