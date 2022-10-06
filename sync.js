/* if the document is ready... */
$(document).ready(function(){

/* if HTML5 video is supported */
  if($('video').attr('canPlayType')){
    
    $('aside::first').append('');

    // Timestamps is an array of N arrays:
    // - first index is the "vid-id"
    // - each is a variable length array of timestamps
    var timestamps = [];
    // N is hardcoded here to 9.
    for (let i = 0; i < 9; i++) {
      timestamps.push([]);
    };

/* hide all articles via CSS */
    $('html').addClass('js');

/* 
   Loop over the articles, read the timestamp start and end and store 
   them in an array
*/
    $('article').each(function(o){
      if($(this).attr('data-start')){
        if($(this).attr('vid-id')) {
          timestamps[$(this).attr('vid-id')].push({
            start : +$(this).attr('data-start'),
            end : +$(this).attr('data-end'),
            elm : $(this)
          });
        }
      }
    });

/* 
  when the video is playing, call the 
  showsection function continuously
*/
    $('video').bind('timeupdate',function(event){
      if($(this).attr('vid-id')){
        showsection(parseFloat(this.currentTime), $(this).attr('vid-id'));
      }
    });

/*
  Test if the current time is within the range of any of the 
  defined timestamps and show the appropriate section.
  Hide all others.
*/
    function showsection(t, vid_id){
      for(let i = 0; i < timestamps[vid_id].length; i++){
        if(t >= timestamps[vid_id][i].start && t <= timestamps[vid_id][i].end){
          timestamps[vid_id][i].elm.addClass('current');
        } else {
          timestamps[vid_id][i].elm.removeClass('current');
        }
      }
    };
    
  };
});