package com.mnaenca.app;

import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.DownloadListener;
import android.webkit.URLUtil;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.webkit.WebViewClient;
import android.app.DownloadManager;
import android.net.Uri;
import android.os.Environment;
import android.widget.Toast;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle s) {
        super.onCreate(s);
        getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_RESIZE);
        WebView wv = getBridge().getWebView();
        if(wv != null) {
            WebSettings ws = wv.getSettings();
            ws.setJavaScriptEnabled(true);
            ws.setDomStorageEnabled(true);
            ws.setAllowFileAccess(true);
            ws.setAllowContentAccess(true);
            ws.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
            ws.setMediaPlaybackRequiresUserGesture(false);
            ws.setLoadWithOverviewMode(true);
            ws.setUseWideViewPort(true);
            CookieManager.getInstance().setAcceptCookie(true);
            CookieManager.getInstance().setAcceptThirdPartyCookies(wv, true);
            wv.setDownloadListener((url, ua, cd, mt, cl) -> {
                DownloadManager.Request r = new DownloadManager.Request(Uri.parse(url));
                r.setTitle(URLUtil.guessFileName(url, cd, mt));
                r.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, URLUtil.guessFileName(url, cd, mt));
                r.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED);
                ((DownloadManager)getSystemService(DOWNLOAD_SERVICE)).enqueue(r);
                Toast.makeText(this, "✅ تم التحميل", Toast.LENGTH_SHORT).show();
            });
            wv.setWebChromeClient(new WebChromeClient());
            wv.setWebViewClient(new WebViewClient());
        }
    }
}