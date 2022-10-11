import copy

original_html = """
<!-- Ayzaan, here is the minimal example for synced text -->
            <div class="section method">
                <aside id="video">
                    <video vid-id='0' width="445px" src="video/colors_to_corners_0_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="0" data-start="0.0" data-end="5.933333333333334">
                  <p>push the yellow hexagon to the top right corner</p>
                </article>
                <article vid-id="0" data-start="5.966666666666667" data-end="9.066666666666666">
                  <p>move the yellow heart to the yellow hexagon</p>
                </article>
                <article vid-id="0" data-start="9.1" data-end="15.166666666666666">
                  <p>push the red circle to the bottom right corner</p>
                </article>
                <article vid-id="0" data-start="15.2" data-end="25.333333333333332">
                  <p>move the red star to the red circle</p>
                </article>
                <article vid-id="0" data-start="25.366666666666667" data-end="34.93333333333333">
                  <p>push the green star to the bottom left corner</p>
                </article>
                <article vid-id="0" data-start="34.96666666666667" data-end="38.36666666666667">
                  <p>move the green circle to the bottom left corner</p>
                </article>
                <article vid-id="0" data-start="38.4" data-end="44.266666666666666">
                  <p>nudge the green star down and left a bit</p>
                </article>
                <article vid-id="0" data-start="44.3" data-end="47.5">
                  <p>nudge the green circle closer to the green star</p>
                </article>
                <article vid-id="0" data-start="47.53333333333333" data-end="54.733333333333334">
                  <p>move the blue cube to the top left corner</p>
                </article>
                <article vid-id="0" data-start="54.766666666666666" data-end="62.833333333333336">
                  <p>push the blue triangle slowly to the blue cube</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="1" width="445px" src="video/colors_to_corners_1_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="1" data-start="0.0" data-end="8.966666666666667">
                  <p>move the green star to the bottom right corner</p>
                </article>
                <article vid-id="1" data-start="9.0" data-end="18.933333333333334">
                  <p>push the green circle to the green star</p>
                </article>
                <article vid-id="1" data-start="18.966666666666665" data-end="23.366666666666667">
                  <p>move the red circle to the bottom left corner</p>
                </article>
                <article vid-id="1" data-start="23.4" data-end="27.233333333333334">
                  <p>push the red star to the red circle</p>
                </article>
                <article vid-id="1" data-start="27.266666666666666" data-end="36.56666666666667">
                  <p>move the blue triangle to the top left corner</p>
                </article>
                <article vid-id="1" data-start="36.6" data-end="45.36666666666667">
                  <p>push the blue cube to the blue triangle</p>
                </article>
                <article vid-id="1" data-start="45.4" data-end="53.833333333333336">
                  <p>move the yellow hexagon to the top right</p>
                </article>
                <article vid-id="1" data-start="53.86666666666667" data-end="60.333333333333336">
                  <p>move the heart to the hexagon</p>
                </article>
                <article vid-id="1" data-start="60.36666666666667" data-end="62.43333333333333">
                  <p>nudge the green star closer to the green circle</p>
                </article>
                <article vid-id="1" data-start="62.46666666666667" data-end="68.23333333333333">
                  <p>nudge the green blocks to the bottom right corner</p>
                </article>
                <article vid-id="1" data-start="68.26666666666667" data-end="69.93333333333334">
                  <p>move the green star right</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="2" width="445px" src="video/colors_to_corners_2_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="2" data-start="0.0" data-end="4.8">
                  <p>move the red circle to the bottom left corner</p>
                </article>
                <article vid-id="2" data-start="4.833333333333333" data-end="16.533333333333335">
                  <p>move the red star to the red circle</p>
                </article>
                <article vid-id="2" data-start="16.566666666666666" data-end="21.333333333333332">
                  <p>nudge the red star closer to the red circle</p>
                </article>
                <article vid-id="2" data-start="21.366666666666667" data-end="28.0">
                  <p>push the green circle to the top left corner</p>
                </article>
                <article vid-id="2" data-start="28.033333333333335" data-end="38.06666666666667">
                  <p>move the green star to the green circle</p>
                </article>
                <article vid-id="2" data-start="38.1" data-end="44.333333333333336">
                  <p>push the yellow heart to the top right corner</p>
                </article>
                <article vid-id="2" data-start="44.36666666666667" data-end="52.8">
                  <p>move the yellow hexagon to the yellow heart</p>
                </article>
                <article vid-id="2" data-start="52.833333333333336" data-end="60.53333333333333">
                  <p>push the blue cube to the bottom right corner</p>
                </article>
                <article vid-id="2" data-start="60.56666666666667" data-end="75.0">
                  <p>move the blue triangle to the blue cube</p>
                </article>
                <article vid-id="2" data-start="75.03333333333333" data-end="75.83333333333333">
                  <p>touch the right side of the yellow hexagon</p>
                </article>
                <article vid-id="2" data-start="75.86666666666666" data-end="83.53333333333333">
                  <p>push the blue triangle closer to the blue cube</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="3" width="445px" src="video/line_0_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="3" data-start="0.0" data-end="5.033333333333333">
                  <p>push the red star to the bottom center</p>
                </article>
                <article vid-id="3" data-start="5.066666666666666" data-end="9.8">
                  <p>move the blue triangle to the top side of the red star</p>
                </article>
                <article vid-id="3" data-start="9.833333333333334" data-end="11.666666666666666">
                  <p>nudge the blue triangle left a bit</p>
                </article>
                <article vid-id="3" data-start="11.7" data-end="14.9">
                  <p>nudge the yellow hexagon down a bit</p>
                </article>
                <article vid-id="3" data-start="14.933333333333334" data-end="30.0">
                  <p>push the green circle to the top side of the yellow hexagon</p>
                </article>
                <article vid-id="3" data-start="30.033333333333335" data-end="33.56666666666667">
                  <p>nudge the green circle down a bit</p>
                </article>
                <article vid-id="3" data-start="33.6" data-end="34.6">
                  <p>nudge the green circle right a bit</p>
                </article>
                <article vid-id="3" data-start="34.63333333333333" data-end="41.86666666666667">
                  <p>put the red circle to the top side of the green circle</p>
                </article>
                <article vid-id="3" data-start="41.9" data-end="43.2">
                  <p>nudge the red circle towards the top </p>
                </article>
                <article vid-id="3" data-start="43.233333333333334" data-end="55.0">
                  <p>nudge the green circle right a bit</p>
                </article>
                <article vid-id="3" data-start="55.03333333333333" data-end="57.7">
                  <p>nudge the red circle down a bit</p>
                </article>
                <article vid-id="3" data-start="57.733333333333334" data-end="60.53333333333333">
                  <p>push the yellow heart to the top side of the red circle</p>
                </article>
                <article vid-id="3" data-start="60.56666666666667" data-end="62.733333333333334">
                  <p>move the yellow heart to the top side of the red circle</p>
                </article>
                <article vid-id="3" data-start="62.766666666666666" data-end="66.5">
                  <p>nudge the yellow heart down a bit</p>
                </article>
                <article vid-id="3" data-start="66.53333333333333" data-end="68.96666666666667">
                  <p>push the green star to the top side of the yellow heart</p>
                </article>
                <article vid-id="3" data-start="69.0" data-end="75.5">
                  <p>nudge the green star left a bit</p>
                </article>
                <article vid-id="3" data-start="75.53333333333333" data-end="77.6">
                  <p>nudge the green star up a bit</p>
                </article>
                <article vid-id="3" data-start="77.63333333333334" data-end="79.16666666666667">
                  <p>move the green star up and left</p>
                </article>
                <article vid-id="3" data-start="79.2" data-end="80.83333333333333">
                  <p>touch the left side of the green star</p>
                </article>
                <article vid-id="3" data-start="80.86666666666666" data-end="82.06666666666666">
                  <p>nudge the green star right a bit</p>
                </article>
                <article vid-id="3" data-start="82.1" data-end="88.83333333333333">
                  <p>push the blue cube to the top side of the green star</p>
                </article>
                <article vid-id="3" data-start="88.86666666666666" data-end="98.2">
                  <p>nudge the blue cube down a bit</p>
                </article>
                <article vid-id="3" data-start="98.23333333333333" data-end="99.4">
                  <p>nudge the blue cube to the right</p>
                </article>
                <article vid-id="3" data-start="99.43333333333334" data-end="112.86666666666666">
                  <p>nudge the blue cube right a bit</p>
                </article>
                <article vid-id="3" data-start="112.9" data-end="114.3">
                  <p>nudge the blue cube down and right</p>
                </article>
                <article vid-id="3" data-start="114.33333333333333" data-end="115.9">
                  <p>nudge the blue cube down</p>
                </article>
                <article vid-id="3" data-start="115.93333333333334" data-end="131.2">
                  <p>nudge the blue cube right</p>
                </article>
                <article vid-id="3" data-start="131.23333333333332" data-end="134.83333333333334">
                  <p>slide the blue cube right</p>
                </article>
                <article vid-id="3" data-start="134.86666666666667" data-end="143.73333333333332">
                  <p>nudge the blue cube towards the right side</p>
                </article>
                <article vid-id="3" data-start="143.76666666666668" data-end="146.23333333333332">
                  <p>touch the left side of the blue cube</p>
                </article>
                <article vid-id="3" data-start="146.26666666666668" data-end="148.6">
                  <p>nudge the blue cube right</p>
                </article>
                <article vid-id="3" data-start="148.63333333333333" data-end="150.66666666666666">
                  <p>nudge the blue cube up</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="4" width="445px" src="video/line_1_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="4" data-start="0.0" data-end="7.866666666666666">
                  <p>move the red circle to the bottom center</p>
                </article>
                <article vid-id="4" data-start="7.9" data-end="9.6">
                  <p>move the red circle right a bit</p>
                </article>
                <article vid-id="4" data-start="9.633333333333333" data-end="11.433333333333334">
                  <p>nudge the red circle down</p>
                </article>
                <article vid-id="4" data-start="11.466666666666667" data-end="17.0">
                  <p>push the red circle to the bottom side of the board</p>
                </article>
                <article vid-id="4" data-start="17.033333333333335" data-end="20.9">
                  <p>push the red circle to the bottom center</p>
                </article>
                <article vid-id="4" data-start="20.933333333333334" data-end="25.8">
                  <p>push the green circle to the top side of the red circle</p>
                </article>
                <article vid-id="4" data-start="25.833333333333332" data-end="28.766666666666666">
                  <p>nudge the green circle left</p>
                </article>
                <article vid-id="4" data-start="28.8" data-end="41.766666666666666">
                  <p>nudge the green circle right</p>
                </article>
                <article vid-id="4" data-start="41.8" data-end="48.36666666666667">
                  <p>push the green circle right a bit</p>
                </article>
                <article vid-id="4" data-start="48.4" data-end="61.6">
                  <p>move the blue triangle to the top side of the green circle</p>
                </article>
                <article vid-id="4" data-start="61.63333333333333" data-end="70.83333333333333">
                  <p>nudge the blue triangle down a bit</p>
                </article>
                <article vid-id="4" data-start="70.86666666666666" data-end="72.7">
                  <p>nudge the green circle left a bit</p>
                </article>
                <article vid-id="4" data-start="72.73333333333333" data-end="73.93333333333334">
                  <p>move the red circle closer to the bottom side of the green circle</p>
                </article>
                <article vid-id="4" data-start="73.96666666666667" data-end="75.26666666666667">
                  <p>touch the blue cube</p>
                </article>
                <article vid-id="4" data-start="75.3" data-end="77.03333333333333">
                  <p>nudge the blue triangle left</p>
                </article>
                <article vid-id="4" data-start="77.06666666666666" data-end="87.56666666666666">
                  <p>push the blue cube to the top side of the blue triangle</p>
                </article>
                <article vid-id="4" data-start="87.6" data-end="94.86666666666666">
                  <p>nudge the blue cube left</p>
                </article>
                <article vid-id="4" data-start="94.9" data-end="96.63333333333334">
                  <p>touch the top side of the red star</p>
                </article>
                <article vid-id="4" data-start="96.66666666666667" data-end="106.5">
                  <p>push the yellow heart to the top side of the red star</p>
                </article>
                <article vid-id="4" data-start="106.53333333333333" data-end="108.13333333333334">
                  <p>nudge the yellow heart left</p>
                </article>
                <article vid-id="4" data-start="108.16666666666667" data-end="109.56666666666666">
                  <p>touch the left side of the yellow heart</p>
                </article>
                <article vid-id="4" data-start="109.6" data-end="110.46666666666667">
                  <p>nudge the yellow heart right a bit</p>
                </article>
                <article vid-id="4" data-start="110.5" data-end="121.76666666666667">
                  <p>put the yellow hexagon to the top side of the yellow heart</p>
                </article>
                <article vid-id="4" data-start="121.8" data-end="123.2">
                  <p>nudge the yellow hexagon right a bit</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="5" width="445px" src="video/line_2_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="5" data-start="0.0" data-end="10.733333333333333">
                  <p>push the green star to the bottom center</p>
                </article>
                <article vid-id="5" data-start="10.766666666666667" data-end="15.833333333333334">
                  <p>move the green circle to the top side of the green star</p>
                </article>
                <article vid-id="5" data-start="15.866666666666667" data-end="23.633333333333333">
                  <p>move the red circle to the top side of the green circle</p>
                </article>
                <article vid-id="5" data-start="23.666666666666668" data-end="27.766666666666666">
                  <p>nudge the red circle right a bit</p>
                </article>
                <article vid-id="5" data-start="27.8" data-end="36.8">
                  <p>move the red star to the top side of the red circle</p>
                </article>
                <article vid-id="5" data-start="36.833333333333336" data-end="38.56666666666667">
                  <p>move the yellow heart up and left away from the red circle</p>
                </article>
                <article vid-id="5" data-start="38.6" data-end="40.0">
                  <p>push the yellow heart up</p>
                </article>
                <article vid-id="5" data-start="40.03333333333333" data-end="41.1">
                  <p>move the yellow heart up</p>
                </article>
                <article vid-id="5" data-start="41.13333333333333" data-end="48.43333333333333">
                  <p>nudge the red star right a bit</p>
                </article>
                <article vid-id="5" data-start="48.46666666666667" data-end="50.166666666666664">
                  <p>move the yellow heart to the top side of the red star</p>
                </article>
                <article vid-id="5" data-start="50.2" data-end="54.5">
                  <p>push the yellow hexagon to the top side of the yellow heart</p>
                </article>
                <article vid-id="5" data-start="54.53333333333333" data-end="58.8">
                  <p>nudge the yellow hexagon closer to the yellow heart</p>
                </article>
                <article vid-id="5" data-start="58.833333333333336" data-end="70.3">
                  <p>nudge the yellow hexagon left a bit</p>
                </article>
                <article vid-id="5" data-start="70.33333333333333" data-end="74.2">
                  <p>nudge the yellow hexagon to the left</p>
                </article>
                <article vid-id="5" data-start="74.23333333333333" data-end="76.26666666666667">
                  <p>move the blue cube to the top side of the yellow hexagon</p>
                </article>
                <article vid-id="5" data-start="76.3" data-end="80.03333333333333">
                  <p>nudge the blue cube left a bit</p>
                </article>
                <article vid-id="5" data-start="80.06666666666666" data-end="88.23333333333333">
                  <p>move the blue triangle to the top side of the blue cube</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="6" width="445px" src="video/smiley_0_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="6" data-start="0.0" data-end="4.3">
                  <p>move the red circle to the bottom center</p>
                </article>
                <article vid-id="6" data-start="4.333333333333333" data-end="5.366666666666666">
                  <p>push the green star to the center</p>
                </article>
                <article vid-id="6" data-start="5.4" data-end="10.433333333333334">
                  <p>move the heart to the right side of the red star</p>
                </article>
                <article vid-id="6" data-start="10.466666666666667" data-end="12.766666666666667">
                  <p>move the heart to the right side of the red circle</p>
                </article>
                <article vid-id="6" data-start="12.8" data-end="16.633333333333333">
                  <p>push the blue cube to the right side of the heart</p>
                </article>
                <article vid-id="6" data-start="16.666666666666668" data-end="32.166666666666664">
                  <p>move the hexagon between the triangle and red circle</p>
                </article>
                <article vid-id="6" data-start="32.2" data-end="37.8">
                  <p>move the green star to the center</p>
                </article>
                <article vid-id="6" data-start="37.833333333333336" data-end="46.2">
                  <p>push the red star to the right side of the hexagon</p>
                </article>
                <article vid-id="6" data-start="46.233333333333334" data-end="58.56666666666667">
                  <p>move the yellow hexagon left a bit</p>
                </article>
                <article vid-id="6" data-start="58.6" data-end="61.13333333333333">
                  <p>nudge the hexagon left</p>
                </article>
                <article vid-id="6" data-start="61.166666666666664" data-end="74.13333333333334">
                  <p>move the red circle down just a bit</p>
                </article>
                <article vid-id="6" data-start="74.16666666666667" data-end="77.6">
                  <p>push the yellow hexagon between the blue triangle and red circle</p>
                </article>
                <article vid-id="6" data-start="77.63333333333334" data-end="82.8">
                  <p>nudge the hexagon down a bit</p>
                </article>
                <article vid-id="6" data-start="82.83333333333333" data-end="83.86666666666666">
                  <p>move the hexagon towards the bottom</p>
                </article>
                <article vid-id="6" data-start="83.9" data-end="85.93333333333334">
                  <p>touch the green star</p>
                </article>
                <article vid-id="6" data-start="85.96666666666667" data-end="89.6">
                  <p>move the yellow hexagon closer to the blue triangle</p>
                </article>
                <article vid-id="6" data-start="89.63333333333334" data-end="93.16666666666667">
                  <p>move the red star closer to the hexagon</p>
                </article>
                <article vid-id="6" data-start="93.2" data-end="94.66666666666667">
                  <p>nudge the red star down</p>
                </article>
                <article vid-id="6" data-start="94.7" data-end="98.03333333333333">
                  <p>put the yellow hexagon between the triangle and red star</p>
                </article>
                <article vid-id="6" data-start="98.06666666666666" data-end="110.8">
                  <p>nudge the hexagon left a bit</p>
                </article>
                <article vid-id="6" data-start="110.83333333333333" data-end="112.93333333333334">
                  <p>move the blue cube closer to the heart</p>
                </article>
                <article vid-id="6" data-start="112.96666666666667" data-end="118.8">
                  <p>push the hexagon to the top right side of the blue cube</p>
                </article>
                <article vid-id="6" data-start="118.83333333333333" data-end="123.4">
                  <p>nudge the hexagon to the right</p>
                </article>
                <article vid-id="6" data-start="123.43333333333334" data-end="125.06666666666666">
                  <p>move the red star to the top left side of the triangle</p>
                </article>
                <article vid-id="6" data-start="125.1" data-end="127.3">
                  <p>move the red star up a bit</p>
                </article>
                <article vid-id="6" data-start="127.33333333333333" data-end="133.8">
                  <p>nudge the hexagon up a bit</p>
                </article>
                <article vid-id="6" data-start="133.83333333333334" data-end="135.06666666666666">
                  <p>nudge the blue cube up a bit</p>
                </article>
                <article vid-id="6" data-start="135.1" data-end="136.03333333333333">
                  <p>nudge the red star up a bit</p>
                </article>
                <article vid-id="6" data-start="136.06666666666666" data-end="140.36666666666667">
                  <p>point at the green star</p>
                </article>
                <article vid-id="6" data-start="140.4" data-end="141.33333333333334">
                  <p>point at the green circle</p>
                </article>
                <article vid-id="6" data-start="141.36666666666667" data-end="144.76666666666668">
                  <p>nudge the blue triangle up a bit</p>
                </article>
                <article vid-id="6" data-start="144.8" data-end="149.03333333333333">
                  <p>nudge the green star right a bit</p>
                </article>
                <article vid-id="6" data-start="149.06666666666666" data-end="151.2">
                  <p>move the green star up a bit</p>
                </article>
                <article vid-id="6" data-start="151.23333333333332" data-end="158.36666666666667">
                  <p>nudge the green star to the right</p>
                </article>
                <article vid-id="6" data-start="158.4" data-end="159.23333333333332">
                  <p>touch the green circle</p>
                </article>
                <article vid-id="6" data-start="159.26666666666668" data-end="162.26666666666668">
                  <p>move the green star to the center</p>
                </article>
                <article vid-id="6" data-start="162.3" data-end="163.96666666666667">
                  <p>move the green star to the right side of the board</p>
                </article>
                <article vid-id="6" data-start="164.0" data-end="166.53333333333333">
                  <p>nudge the green circle right</p>
                </article>
                <article vid-id="6" data-start="166.56666666666666" data-end="168.8">
                  <p>nudge the green star left</p>
                </article>
                <article vid-id="6" data-start="168.83333333333334" data-end="176.16666666666666">
                  <p>nudge the green circle left a bit</p>
                </article>
                <article vid-id="6" data-start="176.2" data-end="179.06666666666666">
                  <p>move the green circle to the left side</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="7" width="445px" src="video/smiley_1_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                 <article vid-id="7" data-start="0.0" data-end="2.2">
                  <p>push the red star to the bottom center</p>
                </article>
                <article vid-id="7" data-start="2.2333333333333334" data-end="4.833333333333333">
                  <p>move the yellow hexagon to the right side of the red star</p>
                </article>
                <article vid-id="7" data-start="4.866666666666666" data-end="11.133333333333333">
                  <p>push the yellow heart between the red and green stars</p>
                </article>
                <article vid-id="7" data-start="11.166666666666666" data-end="14.7">
                  <p>move the red circle to the right of the yellow hexagon</p>
                </article>
                <article vid-id="7" data-start="14.733333333333333" data-end="19.266666666666666">
                  <p>push the green star to the left of the green circle</p>
                </article>
                <article vid-id="7" data-start="19.3" data-end="27.333333333333332">
                  <p>move the blue triangle to the left of the yellow heart</p>
                </article>
                <article vid-id="7" data-start="27.366666666666667" data-end="29.7">
                  <p>push the green star to the top center</p>
                </article>
                <article vid-id="7" data-start="29.733333333333334" data-end="34.733333333333334">
                  <p>push the green circle to the top center</p>
                </article>
                <article vid-id="7" data-start="34.766666666666666" data-end="36.86666666666667">
                  <p>move the green star left a bit</p>
                </article>
                <article vid-id="7" data-start="36.9" data-end="39.9">
                  <p>push the red star between the yellow heart and yellow hexagon</p>
                </article>
                <article vid-id="7" data-start="39.93333333333333" data-end="45.86666666666667">
                  <p>move the blue cube between the red star and yellow heart</p>
                </article>
                <article vid-id="7" data-start="45.9" data-end="52.0">
                  <p>push the green circle to the right of the green star</p>
                </article>
                <article vid-id="7" data-start="52.03333333333333" data-end="53.333333333333336">
                  <p>move the green blocks to the top center</p>
                </article>
                <article vid-id="7" data-start="53.36666666666667" data-end="58.53333333333333">
                  <p>nudge the green circle left a bit</p>
                </article>
                <article vid-id="7" data-start="58.56666666666667" data-end="63.1">
                  <p>nudge the blue cube down and left a bit</p>
                </article>
                <article vid-id="7" data-start="63.13333333333333" data-end="70.2">
                  <p>nudge the blue cube down a bit</p>
                </article>
                <article vid-id="7" data-start="70.23333333333333" data-end="73.33333333333333">
                  <p>move the yellow heart between the triangle and cube</p>
                </article>
                <article vid-id="7" data-start="73.36666666666666" data-end="74.7">
                  <p>nudge the blue triangle up a bit</p>
                </article>
                <article vid-id="7" data-start="74.73333333333333" data-end="76.66666666666667">
                  <p>move the red star closer to the blue cube</p>
                </article>
                <article vid-id="7" data-start="76.7" data-end="78.4">
                  <p>move the red circle to the right side of the yellow hexagon</p>
                </article>
                <article vid-id="7" data-start="78.43333333333334" data-end="80.7">
                  <p>nuge the hexagon down and right a bit</p>
                </article>
                <article vid-id="7" data-start="80.73333333333333" data-end="83.16666666666667">
                  <p>nudge the yellow hexagon down and right a bit</p>
                </article>
                <article vid-id="7" data-start="83.2" data-end="86.4">
                  <p>slightly nudge the hexagon right</p>
                </article>
                <article vid-id="7" data-start="86.43333333333334" data-end="87.86666666666666">
                  <p>push the hexagon slightly to the right</p>
                </article>
                <article vid-id="7" data-start="87.9" data-end="88.6">
                  <p>touch the green circle</p>
                </article>
                <article vid-id="7" data-start="88.63333333333334" data-end="91.0">
                  <p>nudge the hexagon between the red star and red circle</p>
                </article>
                <article vid-id="7" data-start="91.03333333333333" data-end="91.6">
                  <p>put the yellow hexagon to the bottom side of the red circle</p>
                </article>
                <article vid-id="7" data-start="91.63333333333334" data-end="93.16666666666667">
                  <p>touch the green circle</p>
                </article>
                <article vid-id="7" data-start="93.2" data-end="94.13333333333334">
                  <p>touch the red circle</p>
                </article>
                <article vid-id="7" data-start="94.16666666666667" data-end="96.5">
                  <p>nudge the red star up and left a bit</p>
                </article>
                <article vid-id="7" data-start="96.53333333333333" data-end="98.43333333333334">
                  <p>push the yellow hexagon between the red blocks</p>
                </article>
                <article vid-id="7" data-start="98.46666666666667" data-end="110.06666666666666">
                  <p>nudge the yellow hexagon between the blue cube and red star</p>
                </article>
                <article vid-id="7" data-start="110.1" data-end="121.2">
                  <p>nudge the hexagon left and down a bit</p>
                </article>
                <article vid-id="7" data-start="121.23333333333333" data-end="123.06666666666666">
                  <p>nudge the red star up and right a bit</p>
                </article>
                <article vid-id="7" data-start="123.1" data-end="124.3">
                  <p>push the yellow hexagon closer to the yellow heart</p>
                </article>
                <article vid-id="7" data-start="124.33333333333333" data-end="130.23333333333332">
                  <p>move the blue cube to the right side of the hexagon</p>
                </article>
                <article vid-id="7" data-start="130.26666666666668" data-end="133.36666666666667">
                  <p>push the blue cube to the yellow hexagon</p>
                </article>
                <article vid-id="7" data-start="133.4" data-end="134.76666666666668">
                  <p>nudge the blue cube up</p>
                </article>
                <article vid-id="7" data-start="134.8" data-end="137.46666666666667">
                  <p>put the red circle on the right side of the blue cube</p>
                </article>
                <article vid-id="7" data-start="137.5" data-end="142.26666666666668">
                  <p>nudge the red circle down a bit</p>
                </article>
                <article vid-id="7" data-start="142.3" data-end="144.2">
                  <p>put the red star on the top right side of the red circle</p>
                </article>
                <article vid-id="7" data-start="144.23333333333332" data-end="146.06666666666666">
                  <p>nudge the green star up and right a bit</p>
                </article>
                <article vid-id="7" data-start="146.1" data-end="146.66666666666666">
                  <p>nudge the green star down</p>
                </article>
                <article vid-id="7" data-start="146.7" data-end="150.2">
                  <p>nudge the green star down a bit</p>
                </article>
                <article vid-id="7" data-start="150.23333333333332" data-end="154.83333333333334">
                  <p>nudge the green star right a bit</p>
                </article>
                <article vid-id="7" data-start="154.86666666666667" data-end="157.9">
                  <p>nudge the green star down a bit</p>
                </article>
            </div>
            <div style="clear:both;"></div>
            <div class="section method">
                <aside id="video">
                    <video vid-id="8" width="445px" src="video/smiley_2_sped_up.mp4" playsinline="" muted="" autoplay="" loop="" controls style="float: left; margin-right: 30px; padding-left: 10px; padding-bottom: 10px; padding-top: 7px"></video>        
                </aside>
                <article vid-id="8" data-start="0.0" data-end="19.7">
                  <p>move the heart to the right side of the red circle</p>
                </article>
                <article vid-id="8" data-start="19.733333333333334" data-end="24.9">
                  <p>separate the green star from the heart</p>
                </article>
                <article vid-id="8" data-start="24.933333333333334" data-end="31.266666666666666">
                  <p>move the heart to the right side of the red circle</p>
                </article>
                <article vid-id="8" data-start="31.3" data-end="38.56666666666667">
                  <p>nudge the heart to the right</p>
                </article>
                <article vid-id="8" data-start="38.6" data-end="43.43333333333333">
                  <p>slide the heart right</p>
                </article>
                <article vid-id="8" data-start="43.46666666666667" data-end="49.53333333333333">
                  <p>slide the blue cube to the left side of the red circle</p>
                </article>
                <article vid-id="8" data-start="49.56666666666667" data-end="52.166666666666664">
                  <p>slide the blue cube left</p>
                </article>
                <article vid-id="8" data-start="52.2" data-end="56.9">
                  <p>move the green star to the top center</p>
                </article>
                <article vid-id="8" data-start="56.93333333333333" data-end="62.53333333333333">
                  <p>push the red star to the right side of the yellow heart</p>
                </article>
                <article vid-id="8" data-start="62.56666666666667" data-end="63.36666666666667">
                  <p>move the blue cube to the left side of the red circle</p>
                </article>
                <article vid-id="8" data-start="63.4" data-end="64.83333333333333">
                  <p>slide the red star up</p>
                </article>
                <article vid-id="8" data-start="64.86666666666666" data-end="70.86666666666666">
                  <p>nudge the red star up and right</p>
                </article>
                <article vid-id="8" data-start="70.9" data-end="80.4">
                  <p>push the blue cube to the left side of the red circle</p>
                </article>
                <article vid-id="8" data-start="80.43333333333334" data-end="83.5">
                  <p>bring the blue triangle between the blue cube and red circle</p>
                </article>
                <article vid-id="8" data-start="83.53333333333333" data-end="88.66666666666667">
                  <p>nudge the blue triangle right</p>
                </article>
                <article vid-id="8" data-start="88.7" data-end="107.43333333333334">
                  <p>slide the blue triangle right</p>
                </article>
                <article vid-id="8" data-start="107.46666666666667" data-end="108.06666666666666">
                  <p>separate the blue triangle from </p>
                </article>
                <article vid-id="8" data-start="108.1" data-end="111.43333333333334">
                  <p>nudge the red circle closer to the blue triangle</p>
                </article>
                <article vid-id="8" data-start="111.46666666666667" data-end="112.26666666666667">
                  <p>touch the right side of the red star</p>
                </article>
                <article vid-id="8" data-start="112.3" data-end="113.2">
                  <p>move the green star to the top left corner</p>
                </article>
                <article vid-id="8" data-start="113.23333333333333" data-end="113.96666666666667">
                  <p>touch the right side of the green circle</p>
                </article>
                <article vid-id="8" data-start="114.0" data-end="116.53333333333333">
                  <p>push the green star towards the top left </p>
                </article>
                <article vid-id="8" data-start="116.56666666666666" data-end="117.9">
                  <p>push the green star towards the top left</p>
                </article>
                <article vid-id="8" data-start="117.93333333333334" data-end="121.56666666666666">
                  <p>nudge the blue triangle left</p>
                </article>
                <article vid-id="8" data-start="121.6" data-end="123.06666666666666">
                  <p>touch the right side of the green circle</p>
                </article>
                <article vid-id="8" data-start="123.1" data-end="138.1">
                  <p>nudge the blue triangle down</p>
                </article>
                <article vid-id="8" data-start="138.13333333333333" data-end="141.33333333333334">
                  <p>slide the blue triangle down</p>
                </article>
                <article vid-id="8" data-start="141.36666666666667" data-end="143.63333333333333">
                  <p>move the blue triangle towards the bottom</p>
                </article>
                <article vid-id="8" data-start="143.66666666666666" data-end="144.06666666666666">
                  <p>touch the right side of the green circle</p>
                </article>
                <article vid-id="8" data-start="144.1" data-end="145.23333333333332">
                  <p>nudge the red star up a bit</p>
                </article>
                <article vid-id="8" data-start="145.26666666666668" data-end="146.3">
                  <p>nudge the red star towards the top right</p>
                </article>
                <article vid-id="8" data-start="146.33333333333334" data-end="148.73333333333332">
                  <p>nudge the red star up and right a bit</p>
                </article>
                <article vid-id="8" data-start="148.76666666666668" data-end="169.06666666666666">
                  <p>nudge the red star up and left a bit</p>
                </article>
                <article vid-id="8" data-start="169.1" data-end="172.33333333333334">
                  <p>nudge the red star left</p>
                </article>
                <article vid-id="8" data-start="172.36666666666667" data-end="173.4">
                  <p>nudge the green circle up slightly</p>
                </article>
            </div>
"""

#print(original_html)

lines = original_html.split('\n')
new_lines = []

SPEED_UP_FACTOR = 4.0

for line in lines:
	if "data-start" in line:
		print(line)
		new_line = copy.deepcopy(line)
		# Adjust start
		data_start_val = float(line.split('data-start="')[1].split('"')[0])
		print(data_start_val)
		data_start_new = data_start_val/SPEED_UP_FACTOR
		print(data_start_new)
		before = line.split('data-start="')[0]
		after = line.split('data-start="')[1].split('" ')[1]
		joined = before + f'data-start="{data_start_new}" ' + after
		print(joined)

		# Adjust end
		data_end_val = float(joined.split('data-end="')[1].split('"')[0])
		print(data_end_val)
		data_end_new = data_end_val/SPEED_UP_FACTOR
		before = joined.split('data-end="')[0]
		joined = before + f'data-end="{data_end_new}">'
		new_lines.append(joined)
	else:
		new_lines.append(line)

# open file in write mode
with open(r'out.html', 'w') as fp:
    for new_line in new_lines:
        fp.write("%s\n" % new_line)
    print('Done')
