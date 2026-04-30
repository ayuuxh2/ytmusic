package com.tridermusic.app.di

import com.maxrave.domain.manager.DataStoreManager
import com.maxrave.domain.repository.AlbumRepository
import com.maxrave.domain.repository.CacheRepository
import com.maxrave.domain.repository.LocalPlaylistRepository
import com.maxrave.domain.repository.LyricsCanvasRepository
import com.maxrave.domain.repository.PlaylistRepository
import com.maxrave.domain.repository.SongRepository
import com.maxrave.domain.repository.StreamRepository
import com.maxrave.domain.repository.CommonRepository
import com.maxrave.domain.repository.AnalyticsRepository
import com.tridermusic.app.viewModel.AlbumViewModel
import com.tridermusic.app.viewModel.ArtistViewModel
import com.tridermusic.app.viewModel.HomeViewModel
import com.tridermusic.app.viewModel.LibraryDynamicPlaylistViewModel
import com.tridermusic.app.viewModel.LibraryViewModel
import com.tridermusic.app.viewModel.LocalPlaylistViewModel
import com.tridermusic.app.viewModel.LogInViewModel
import com.tridermusic.app.viewModel.MoodViewModel
import com.tridermusic.app.viewModel.MoreAlbumsViewModel
import com.tridermusic.app.viewModel.NotificationViewModel
import com.tridermusic.app.viewModel.NowPlayingBottomSheetViewModel
import com.tridermusic.app.viewModel.PlaylistViewModel
import com.tridermusic.app.viewModel.PodcastViewModel
import com.tridermusic.app.viewModel.RecentlySongsViewModel
import com.tridermusic.app.viewModel.SearchViewModel
import com.tridermusic.app.viewModel.SettingsViewModel
import com.tridermusic.app.viewModel.SharedViewModel
import org.koin.core.module.dsl.viewModel
import org.koin.dsl.module

val viewModelModule =
    module {
        single {
            SharedViewModel(
                get<DataStoreManager>(),
                get<StreamRepository>(),
                get<SongRepository>(),
                get<AlbumRepository>(),
                get<LocalPlaylistRepository>(),
                get<PlaylistRepository>(),
                get<LyricsCanvasRepository>(),
                get<CacheRepository>(),
                get<CommonRepository>(),
                get<AnalyticsRepository>(),
            )
        }
        single {
            SearchViewModel(
                get(),
                get(),
            )
        }
        viewModel {
            NowPlayingBottomSheetViewModel(
                get(),
                get(),
                get(),
                get(),
            )
        }
        viewModel {
            LibraryViewModel(
                get(),
                get(),
                get(),
                get(),
                get(),
                get(),
                get(),
            )
        }
        viewModel {
            LibraryDynamicPlaylistViewModel(
                get(),
                get(),
            )
        }
        viewModel {
            AlbumViewModel(
                get(),
                get(),
            )
        }
        viewModel {
            HomeViewModel(
                get(),
                get(),
            )
        }
        viewModel {
            SettingsViewModel(
                get(),
                get(),
                get(),
                get(),
                get(),
            )
        }
        viewModel {
            ArtistViewModel(
                get(),
                get(),
            )
        }
        viewModel {
            PlaylistViewModel(
                get(),
                get(),
                get(),
            )
        }
        viewModel {
            LogInViewModel(
                get(),
            )
        }
        viewModel {
            PodcastViewModel(
                get(),
            )
        }
        viewModel {
            MoreAlbumsViewModel(
                get(),
            )
        }
        viewModel {
            RecentlySongsViewModel(
                get(),
            )
        }
        viewModel {
            LocalPlaylistViewModel(
                get(),
                get(),
                get(),
            )
        }
        viewModel {
            NotificationViewModel(
                get(),
            )
        }
        viewModel {
            MoodViewModel(
                get(),
                get(),
            )
        }
    }
