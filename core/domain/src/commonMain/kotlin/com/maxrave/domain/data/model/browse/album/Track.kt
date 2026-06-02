package com.maxrave.domain.data.model.browse.album

import com.maxrave.domain.data.model.searchResult.songs.Album
import com.maxrave.domain.data.model.searchResult.songs.Artist
import com.maxrave.domain.data.model.searchResult.songs.FeedbackTokens
import com.maxrave.domain.data.model.searchResult.songs.Thumbnail
import kotlinx.serialization.Serializable

@Serializable
data class Track(
    val album: Album? = null,
    val artists: List<Artist>? = emptyList(),
    val duration: String? = null,
    val durationSeconds: Int? = null,
    val isAvailable: Boolean = true,
    val isExplicit: Boolean = false,
    val likeStatus: String? = null,
    val thumbnails: List<Thumbnail>? = emptyList(),
    val title: String,
    val videoId: String,
    val videoType: String? = null,
    val category: String? = null,
    val feedbackTokens: FeedbackTokens? = null,
    val resultType: String? = null,
    val year: String? = null,
)