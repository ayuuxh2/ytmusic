package com.tridermusic.app.expect

actual fun getDownloadFolderPath(): String = System.getProperty("user.home") + "/Downloads"