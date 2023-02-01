from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Maou no Hajimekata"

site_url = 'https://lightnovelstranslations.com/maou-no-hajimekata/'


source = """
<div class="su-accordion su-u-trim">
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button">
      <span class="su-spoiler-icon"></span>
      <strong>Volume 1 Stage 1</strong>
    </div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong>
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/prologue/">Prologue</a>
        </strong>
        <br />
        <strong
          ><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-1-first-of-all-lets-accumulate-the-magical-energy/"
            >Chapter&nbsp;1
          </a>
        </strong>
        <br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-1-5-dungeon-explanations/">Chapter 1.5</a></strong
        ><br />
        <strong
          >Chapter 2 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-2-lets-attack-the-neighbourhood-village-part-1/"
            >Part 1</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-2-lets-attack-the-neighbourhood-village-part-2/">Part 2</a>)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-3-lets-obtain-passive-income/">Chapter 3</a></strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-4-lets-prepare-for-a-counter-attack/">Chapter 4</a></strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-4-5-dungeon-commentary/">Chapter 4.5</a></strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-5-lets-capture-the-foolish-intruder/">Chapter 5</a></strong
        ><br />
        <strong
          >Chapter 6 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-6-lets-train-the-pitiful-prisoner-part-1/">Part 1</a>,<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-6-lets-train-the-pitiful-prisoner-part-2/"
            >Part 2</a
          >)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-6-5-dungeon-commentary/">Chapter 6.5</a></strong
        ><br />
        <strong
          >Chapter 7 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-lets-receive-the-sacrificed-pure-young-lady-part-1/"
            >part 1</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-lets-receive-the-sacrificed-pure-young-lady-part-2/"
            >part 2</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-lets-receive-the-sacrificed-pure-young-lady-part-3/"
            >part 3</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-lets-receive-the-sacrificed-pure-young-lady-part-4/"
            >part 4</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-lets-receive-the-sacrificed-pure-young-lady-part-5/"
            >part 5</a
          >)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-7-5-dungeon-commentary/">Chapter 7.5</a></strong
        ><br />
        <strong
          >Chapter 8 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-lets-gather-all-the-evil-henchman-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-part-2-lets-gather-all-the-evil-henchman/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-lets-gather-all-the-evil-henchman-part-3/">Part 3</a>,&nbsp;<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-lets-gather-all-the-evil-henchman-part-4/"
            >Part 4</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-lets-gather-all-the-evil-henchman-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 8 Side Story (<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-side-story-1-lets-have-intercourse-with-the-subordinates/"
            >Part 1</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-side-story-2-lets-have-intercourse-with-the-subordinates/"
            >Part 2</a
          >)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-8-5-dungeon-commentary/">Chapter 8.5</a></strong
        ><br />
        <strong
          >Chapter 9 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-9-lets-invade-the-town-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-9-lets-invade-the-town-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-9-lets-invade-the-town-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-9-lets-invade-the-town-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 10 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-1/"
            >Part 1</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-2/"
            >Part 2</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-5/">Part 5</a
          >,&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-6/"
            >Part 6</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-lets-give-despair-to-the-greedy-adventurers-part-8/">Part 8</a
          >)</strong
        ><br />
        <strong
          >Chapter 10 Side Story (

          <a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-side-story-occasionally-we-should-show-appreciation-to-our-subordinates-part-1/"
            >Part 1&nbsp;</a
          >,
          <a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-side-story-occasionally-we-should-show-appreciation-to-our-subordinates-part-2/"
            >Part 2</a
          >)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-10-5-dungeon-commentary/">Chapter 10.5</a></strong
        ><br />
        <strong
          >Chapter 11 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-1/">Part</a
          ><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-1/"> 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-11-lets-become-the-demon-king-part-6/">Part 6</a>)</strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 1 Stage 2</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong
          >Side Chapter (<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/side-chapter-1-lets-insult-those-who-wish-to-be-the-king-part-1/"
            >Part 1</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/side-chapter-1-lets-insult-those-who-wish-to-be-the-king-part-2/">Part 2</a
          >)</strong
        ><br />
        <strong
          >Chapter 12 (<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-12-lets-meet-with-the-residents-of-the-demonic-cave-part-1/"
            >Part 1</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-12-lets-meet-with-the-residents-of-the-demonic-cave-part-2/"
            >Part 2</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-12-lets-meet-with-the-residents-of-the-demonic-cave-part-3/"
            >Part 3</a
          >)</strong
        ><br />
        <strong
          >Chapter 13 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-1/"
            >Part 1</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-2/">Part 2,</a
          >&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-3/"
            >Part 3</a
          >,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-5/">Part 5</a
          >&nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-lets-capture-the-dungeon-of-the-demon-king-part-6/"
            >Part 6</a
          >)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-13-5-dungeon-commentary/">Chapter 13.5</a></strong
        ><br />
        <strong
          >Chapter 14 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-1/">Part 1</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-8/">Part 8</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-9/">Part 9</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-14-lets-give-the-hero-a-cruel-death-part-10/">Part 10</a>)</strong
        ><br />
        <strong
          >Chapter 15 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-15-lets-paint-a-chaotic-picture-of-hell-part-1/"
            >Part 1</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-15-lets-paint-a-chaotic-picture-of-hell-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-15-lets-paint-a-chaotic-picture-of-hell-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-15-lets-paint-a-chaotic-picture-of-hell-part-4/">Part 4</a>)</strong
        ><br />
        <strong>
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-15-5-dungeon-commentary/"> Chapter 15.5 </a>
        </strong>
        <br />
        <strong
          >Chapter 16 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-16-lets-punish-the-fools-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-16-lets-punish-the-fools-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-16-lets-punish-the-fools-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-16-lets-punish-the-fools-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-16-lets-punish-the-fools-part-5/">Part 5</a>)</strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 1 Stage 3</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <div class="code-block code-block-37" style="margin: 8px 0; clear: both">
        <!-- Tag ID: lightnoveltranslations_300x250_728x90_InContent_2 -->
        <div align="center" id="lightnoveltranslations_300x250_728x90_InContent_2">
          <script data-cfasync="false" type="text/javascript">
            freestar.config.enabled_slots.push({
              placementName: "lightnoveltranslations_300x250_728x90_InContent_2",
              slotId: "lightnoveltranslations_300x250_728x90_InContent_2",
            });
          </script>
        </div>
      </div>
      <p>
        <strong
          >Chapter 17 (
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-4/">Part 4</a>&nbsp;<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-part-5/"
            >Part 5</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/chapter-17-lets-draw-our-bows-towards-heaven-part-7/">Part 7</a> )</strong
        ><br />
        <strong
          >Side Story Chapter 3 (<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/side-story-chapter-3-lets-prepare-for-the-final-battle-part-1/"
            >Part 1</a
          >,
          <a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-side-story-chapter-3-lets-prepare-for-the-final-battle-part-2/"
            >Part2</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-side-story-3-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-side-story-3-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-side-story-3-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-side-story-3-part-6/">Part 6</a
          >)</strong
        ><br />
        <strong
          ><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-5-part-1/"
            ><span>Chapter 17.5</span></a
          >
        </strong>

        <br />
        <strong
          >Final Chapter (<a
            href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-chapter-17-final-chapter-part-1/"
            >Part 1</a
          >, <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-part-8/">Part 8</a>)</strong
        ><br />
        <strong>
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-epilogue/"><span>Epilogue</span></a>
        </strong>
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Inter-volume materials</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
        <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>extra</strong></div>
        <div class="su-spoiler-content su-u-clearfix su-u-trim">
          <strong
            ><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-chapter-dungeon-commentary/"
              >Dungeon Commentary</a
            ></strong
          ><br />
          <strong
            ><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-bonus-chapter/">Bonus Chapter</a></strong
          ><br />
          <strong
            >Extra (

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-1/">Chapter 1</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-2/">Chapter 2</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-3/">Chapter 3</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-4/">Chapter 4</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-5/">Chapter 5</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-6/">Chapter 6</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-7/">Chapter 7</a>,

            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-extra-chapter-8/">Chapter 8</a>) </strong
          ><br />
          <strong
            >Final Act (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-1-final-act/">Final Act</a>)</strong
          >
          <p></p>
        </div>
      </div>
      <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
        <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Anniversary</strong></div>
        <div class="su-spoiler-content su-u-clearfix su-u-trim">
          <strong
            >And so the Succubus Girl Smiled(
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/and-so-the-succubus-girl-smiled-part-1/">Part 1</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/and-so-the-succubus-girl-smiled-part-2/">Part 2</a>)</strong
          >
          <p></p>
        </div>
      </div>
      <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
        <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume Release Countdown</strong></div>
        <div class="su-spoiler-content su-u-clearfix su-u-trim">
          <strong>
            Count down(
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/9-the-aged-demon-lord-and-the-young-blue-silver-sorceress/">9</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/8-the-alv-priestess-and-the-demon-lord-apprentice/">8</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/7-crimson-haired-green-eyed-swordswoman/">7</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/6-succubus-alv-and-the-beast-lord/">6</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/5-black-and-white-alv-princesses/">5</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/4-the-little-girl-and-the-big-sister/">4</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/3-the-beloved-girl-and-a-considerate-evil-demon/">3</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/2-demon-lord-and-the-demon-fiancee/">2</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/1-the-house-watching-demon/">1</a>,
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/0-the-girls-who-surround-the-demon-lord/">0</a>)<br />
          </strong>
        </div>
      </div>
      <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
        <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Cut scenes</strong></div>
        <div class="su-spoiler-content su-u-clearfix su-u-trim">
          <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/cut-out-erotic-scenes/">Cut Out Erotic Scenes</a><br /> </strong>
        </div>
      </div>
      <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
        <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Celebratory</strong></div>
        <div class="su-spoiler-content su-u-clearfix su-u-trim">
          <strong
            ><br />
            <a href="https://lightnovelstranslations.com/maou-no-hajimekata/an-alluring-scheme/">An Alluring Scheme</a></strong
          >
          <p></p>
        </div>
      </div>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 2 Stage 1</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-prologue/">Volume 2 Prologue</a></strong
        ><br />
        <strong
          >Chapter 1(<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-1-part-7/">Part 7</a>)</strong
        ><br />
        <strong
          >Interlude 1 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-part-2/">Part 2</a>)</strong
        ><br />
        <strong
          >Chapter 2 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-2-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-2-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-2-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-2-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-2-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 3 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-3-part-6/">Part 6</a>)</strong
        ><br />
        <strong
          >Side Story (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-side-story-1-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-side-story-1-part-2/">Part 2</a>)</strong
        ><br />
        <strong
          >Chapter 4 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-8/">Part 8</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-4-part-9/">Part 9</a>)</strong
        ><br />
        <strong
          >Interlude 2 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-2-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-2-part-2/">Part 2</a>)</strong
        ><br />
        <strong
          >Chapter 5 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-5-part-6/">Part 6</a>)</strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 2 Stage 2</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong
          >Interlude 3 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-3-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-3-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-3-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-3-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-3-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 6 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-6-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-6-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-6-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-6-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-6-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 7 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-7-part-6/">Part 6</a>)</strong
        ><br />
        <strong
          >Chapter 8 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-8-part-6/">Part 6</a>)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-interlude-4/">Interlude 4</a></strong
        ><br />
        <strong
          >Chapter 9 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-9-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-9-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-9-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-9-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-9-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 10 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-10-part-7/">Part 7</a>)</strong
        ><br />
        <strong
          >Chapter 11 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-11-part-7/">Part 7</a></strong
        ><strong>)</strong><br />
        <strong>
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-epilogue-of-part-1/">Epilogue</a></strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 2 Stage 3</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <div class="code-block code-block-39" style="margin: 8px 0; clear: both">
        <!-- Tag ID: lightnoveltranslations_300x250_728x90_InContent_3 -->
        <div align="center" id="lightnoveltranslations_300x250_728x90_InContent_3">
          <script data-cfasync="false" type="text/javascript">
            freestar.config.enabled_slots.push({
              placementName: "lightnoveltranslations_300x250_728x90_InContent_3",
              slotId: "lightnoveltranslations_300x250_728x90_InContent_3",
            });
          </script>
        </div>
      </div>
      <p>
        <strong
          >Chapter 12 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-12-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-12-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-12-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-12-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 13 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-13-part-1/">Part 1</a>,
          &nbsp;<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-13-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-13-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-13-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-13-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 14 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-8/">Part 8</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-14-part-9/">Part 9</a>)</strong
        ><br />
        <strong
          >Chapter 15 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-15-part-7/">Part 7</a>)</strong
        ><br />
        <strong
          >Chapter 16 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-16-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-16-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-16-part-3/">Part 3</a>)</strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 2 Stage 4</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong
          >Chapter 17 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-17-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-17-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-17-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-17-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 18 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-18-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-18-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-18-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-18-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 19 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-19-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-19-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-19-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-19-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 20 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-20-part-8/">Part 8</a>)</strong
        ><br />
        <strong
          >Chapter 21 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-8/">Part 8</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-9/">Part 9</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-10/">Part 10</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-chapter-21-part-11/">Part 11</a>)<br />
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-2-epilogue/">Epilogue</a></strong
        >
      </p>
    </div>
  </div>
  <div class="su-spoiler su-spoiler-style-default su-spoiler-icon-plus su-spoiler-closed" data-scroll-offset="0" data-anchor-in-url="no">
    <div class="su-spoiler-title" tabindex="0" role="button"><span class="su-spoiler-icon"></span><strong>Volume 3 Stage 1</strong></div>
    <div class="su-spoiler-content su-u-clearfix su-u-trim">
      <p>
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-prologue/">Prologue</a></strong
        ><br />
        <strong
          >Chapter 1 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-1-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-1-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-1-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-1-part-4/">Part 4</a>)</strong
        ><br />
        <strong
          >Chapter 2 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-2-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-2-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-2-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-2-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-2-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 3 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-3-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-3-part-2/">Part 2</a>)</strong
        ><br />
        <strong
          >Chapter 4 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-6/">Part 6</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-7/">Part 7</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-4-part-8/">Part 8</a>)</strong
        ><br />
        <strong
          >Chapter 5 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-5-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-5-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-5-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-5-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-5-part-5/">Part 5</a>)</strong
        ><br />
        <strong
          >Chapter 6 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-6-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-6-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-6-part-3/">Part 3</a>)</strong
        ><br />
        <strong
          >Chapter 7 (<a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-1/">Part 1</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-2/">Part 2</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-3/">Part 3</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-4/">Part 4</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-5/">Part 5</a>,
          <a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-chapter-7-part-6/">Part 6</a>)</strong
        ><br />
        <strong><a href="https://lightnovelstranslations.com/maou-no-hajimekata/maou-no-hajimekata-volume-3-epilogue/">Epilogue</a></strong>
      </p>
    </div>
  </div>
</div>



"""

try:
    # source = requests.get(site_url)
    # source.raise_for_status()

    # soup = BeautifulSoup(source.text, 'html.parser')
    soup = BeautifulSoup(source, 'html.parser')

    volumeList = soup.find_all('div', class_='su-spoiler-title')
    volumeContentList = soup.find_all('div', class_='su-spoiler-content')

    i = 0
    for volumeContent in volumeContentList:
        volTitle = volumeList[i].get_text(strip=True)
        i += 1
        # print(volTitle)  # Volume 1 Stage 1

        if volTitle != 'Inter-volume materials':
            ChapterList = volumeContent.find_all('strong')
            for chapter in ChapterList:
                chTitle = chapter.get_text(strip=True)
                # print(chTitle) # Chapter 1 (part1,part 2)
                OnlyChTitle = chTitle.split("(")[0].strip()
                # print(OnlyChTitle) # Chapter 1

                ChapterParts = chapter.find_all('a')
                brk = chTitle.find("(")

                for part in ChapterParts:
                    if brk == -1:
                        partTitle = ""
                        fullPartTitle = OnlyChTitle
                    else:
                        partTitle = part.get_text(strip=True)
                        fullPartTitle = f'{OnlyChTitle} - {partTitle}'

                    partLink = part.get('href')
                    print(volTitle, fullPartTitle, partLink)
                    sheet.append([volTitle, fullPartTitle, partLink])


except Exception as e:
    print(e)


excel.save('Maou no Hajimekata Table of Contents.xlsx')
