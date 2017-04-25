#!/usr/bin/sh
# two-way sync with google drive

RCLONE=rclone sync
REMOTE=remote

# prep
mkdir /tmp/{home_bk,offline}
rsync -aAXv --exclude={.cache/chromium,.cache-bk,.ccache,.chromium-bk,.config/chromium,abs,android,documents,download,gdrive,git,music,phone,pictures,scripts,videos}/ $HOME/ /tmp/home_bk/
rsync -aAXv --exclude={keys,vault} $HOME/documents/ /tmp/offline

# local to gdrive
$RCLONE $HOME/abs/ $REMOTE:abs/			# initial done
#android
$RCLONE /tmp/home_bk/ $REMOTE:home_bk/		# initial done
$RCLONE $HOME/download/ $REMOTE:download/	# initial done
$RCLONE $HOME/music/ $REMOTE:music/		# initial done
$RCLONE /tmp/offline/ $REMOTE:offline/		# initial done
$RCLONE $HOME/phone/ $REMOTE:phone/		# initial done
$RCLONE $HOME/pictures/ $REMOTE:pictures/	# initial done
$RCLONE $HOME/videos/ $REMOTE:videos/		# initial done

# gdive to local, above directories have been simlinked
$RCLONE remote:/ $HOME/gdrive/

# clean up
rm -r /tmp/{home_bk,offline}
