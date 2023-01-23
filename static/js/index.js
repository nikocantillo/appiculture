/*Youtube video handler*/
let videoId = "HyIEZPubbEk";
var player;

// let videoToChange = document.getElementById('list-video');
// videoToChange.addEventListener("click", selectVideo, false);


/*Functions to set the YouTube video*/
function onYouTubeIframeAPIReady() {
  player = new YT.Player('selectedVideo', {
    height: '100%',
    width: '100%',
    videoId: videoId,
    events: {
      'onReady': onPlayerReady,
    }
  });

  function onPlayerReady(event) {
    event.target.playVideo();
  }
}

function selectVideo(newVideoId){
  videoId = newVideoId;
  player.loadVideoById(videoId)
}