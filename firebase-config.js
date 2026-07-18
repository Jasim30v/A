// 💎 MNAENCA 2026 - Luxury Pink Configuration
// Firebase: muvg-42126 | Cloudinary: dmqyd0haj
// ✨ PREMIUM: TikTok Comments + Share System + Left Watermark + Enhanced Profile + Voice Messages

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
const CLOUDINARY_UPLOAD_IMAGE_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`;
const CLOUDINARY_UPLOAD_AUDIO_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/video/upload`;

// 💎 MNAENCA Settings
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #831843, #be185d, #ec4899)",
    "linear-gradient(135deg, #4c0519, #9d174d, #be185d)",
    "linear-gradient(135deg, #9d174d, #db2777, #f472b6)",
    "linear-gradient(135deg, #701a75, #a21caf, #d946ef)",
    "linear-gradient(135deg, #be185d, #ec4899, #fbcfe8)",
    "linear-gradient(135deg, #0a0014, #2d002f, #9d174d)"
];

// 💎 App Info
const APP_NAME = "MNAENCA";
const APP_VERSION = "2026.5";
const PRIMARY_COLOR = "#ec4899";
const SECONDARY_COLOR = "#f472b6";
const WATERMARK_TEXT = "🌸 MNAENCA";
const WATERMARK_URL = "https://res.cloudinary.com/dmqyd0haj/image/upload/v1/watermark_mnaenca";

console.log('💎 %c'+APP_NAME+' v'+APP_VERSION+' Ready ✨', 'color: #ec4899; font-size: 16px; font-weight: bold;');
