#### True instruction:

* https://www.debian.org/doc/manuals/securing-debian-howto/

#### Some essentials:

- [ ] install `harden` package. It have set of virtual packages that conflict with another package that are consiedered unsecure.
- [ ] use `bastille linux`: http://bastille-linux.sourceforge.net/
- [ ] use `nmap localhost` to localize open ports and shut down unused services
- [ ] remove unused packages:
    ```
    dpkg --list
    dpkg --info packageName
    apt-get remove packageName
    ```
- [ ] keep kernel and software up to date
- [ ] install (and use) SELinux