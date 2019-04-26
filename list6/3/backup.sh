# static dump/restore
pg_dump postgres > backup
psql postgres < backup


# filesystem level backup

tar -cf backup.tar /var/lib/postgresql/11/main

# make base backup for WAL
pg_basebackup -D '/home/wojtek/Dokumenty/Semestr10/Security/list6/3/base_backup'

# write ahead log (WAL)
# https://www.postgresql.org/docs/current/continuous-archiving.html

# write settings (to allow backups - all completed wal files will be copied to by backup dir)
cp postgresql.conf /var/lib/postgresql/11/main/postgresql.conf

# now we have backups
# lets restore
sudo /etc/init.d/postgresql stop
cp /var/lib/postgresql/11/main/pg_wal current_pg_wal
rm -rf /var/lib/postgresql/11/main/
cp -r base_backup /var/lib/postgresql/11/main
# check if there are wal files in current_pg_wal that are not present in database wal directory. If so, copy it there
cp recovery.conf /var/lib/postgresql/11/main/
# now start server and let postgres do the job
sudo /etc/init.d/postgresql start
# we should have now recovery.done file instead of recovery.conf
