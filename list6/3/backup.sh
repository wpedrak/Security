# static dump/restore
pg_dump postgres > backup
psql postgres < backup


# filesystem level backup

tar -cf backup.tar /var/lib/postgresql/11/main

# make base backup for WAL
pg_basebackup -D '/home/wojtek/Dokumenty/Semestr10/Security/list6/3/base_backup'

# write ahead log (WAL)
# https://www.postgresql.org/docs/9.1/continuous-archiving.html

# write settings
cp postgresql.conf /var/lib/postgresql/11/main/postgresql.conf
