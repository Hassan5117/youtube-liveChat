import React from 'react';

function YouTubeEmbed({ url }) {
    // Extract video ID and start time from the URL
    const urlParams = new URLSearchParams(new URL(url).search);
    const videoId = urlParams.get('v');
    const startTime = urlParams.get('start');

    let embedUrl = `https://www.youtube.com/embed/${videoId}`;

    if (startTime) {
        embedUrl += `?start=${startTime}`;
    }

    return (
        <iframe 
            width="560" 
            height="315" 
            src={embedUrl} 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen
        ></iframe>
    );
}

export default YouTubeEmbed;
