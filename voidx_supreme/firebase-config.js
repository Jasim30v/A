// 💜 VØID_X 2026 - Supreme Admin Configuration
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
const CLOUDINARY_UPLOAD_URL = `https://api.cloudinary.com/v1_1/${CLOUD_NAME}/auto/upload`;

const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #1a000d, #2d0020, #4a0030)",
    "linear-gradient(135deg, #0d001a, #200030, #350050)",
    "linear-gradient(135deg, #1a0020, #2d0040, #4a0060)",
    "linear-gradient(135deg, #150020, #280040, #3d0060)",
    "linear-gradient(135deg, #200030, #3d0060, #5a0090)",
    "linear-gradient(135deg, #0a0a1a, #1a1040, #2d1a60)"
];

const APP_NAME = "VØID_X";
const PRIMARY_COLOR = "#ff007f";
const WATERMARK_TEXT = "VØID_X SUPREME";

console.log('%c💜 %c'+APP_NAME+' Supreme Ready ✨', 'color: #ff007f; font-size: 16px; font-weight: bold;');
