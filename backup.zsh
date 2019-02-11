# backup script for manㄠally selected files adn folders
while getopts h:d:w:m: option
do
    case "${option}"
        in
        h) rsync --progress -a $(cat /mnt/EXT/.backups/patrick/.hourly) /mnt/EXT/.backups/patrick/ & \
            rsync --progress -a $(cat /mnt/USBHDD/.backups/patrick/.hourly) /mnt/USBHDD/.backups/patrick/;;
        d) rsync --progress -a $(cat /mnt/EXT/.backups/patrick/.daily) /mnt/EXT/.backups/patrick/ & \
            rsync --progress -a $(cat /mnt/USBHDD/.backups/patrick/.daily) /mnt/USBHDD/.backups/patrick/;;
        w) rsync --progress -a $(cat /mnt/EXT/.backups/patrick/.weekly) /mnt/EXT/.backups/patrick/ & \
            rsync --progress -a $(cat /mnt/USBHDD/.backups/patrick/.weekly) /mnt/USBHDD/.backups/patrick/;;
        m) rsync --progress -a $(cat /mnt/EXT/.backups/patrick/.monthly) /mnt/EXT/.backups/patrick/ & \
            rsync --progress -a $(cat /mnt/USBHDD/.backups/patrick/.monthly) /mnt/USBHDD/.backups/patrick/;;
    esac
done
