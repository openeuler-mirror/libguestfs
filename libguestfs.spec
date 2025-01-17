%global _changelog_trimtime %(date +%s -d "2 years ago")
%{?perl_default_filter}
%undefine _strict_symbol_defs_build

Name:          libguestfs
Version:       1.49.5
Release:       2
Epoch:         1
Summary:       A set of tools for accessing and modifying virtual machine (VM) disk images
License:       LGPLv2+
URL:           http://libguestfs.org/
Source0:       https://download.libguestfs.org/1.49-development/libguestfs-1.49.5.tar.gz
Source1:       guestfish.sh
Source2:       yum.conf.in
Patch0001:     001-port-to-php-8.0.0.patch
Patch0002:     fix-not-striped.patch
Patch0003:     support_OPENEULER_to_configure.patch

BuildRequires: gcc-c++, rpcgen, libtirpc-devel, supermin-devel >= 5.1.18, hivex-devel >= 1.2.7-7, ocaml-hivex-devel, perl(Pod::Simple), perl(Pod::Man)
BuildRequires: /usr/bin/pod2text, po4a, augeas-devel >= 1.7.0, readline-devel, genisoimage, libxml2-devel, createrepo, glibc-static, libselinux-utils
BuildRequires: libselinux-devel, fuse, fuse-devel, pcre-devel, file-devel, libvirt-devel, gperf, flex, bison, libdb-utils, cpio, libconfig-devel, xz-devel
BuildRequires: zip, unzip, systemd-units, netpbm-progs, icoutils, libvirt-daemon-qemu, perl(Expect), libacl-devel, libcap-devel, libldm-devel, jansson-devel
BuildRequires: systemd-devel, bash-completion, /usr/bin/ping, /usr/bin/wget, curl, xz, gtk3-devel, dbus-devel, /usr/bin/qemu-img
BuildRequires:  ocaml, ocaml-ocamldoc, ocaml-findlib-devel, ocaml-gettext-devel, ocaml-ounit-devel, ocaml-libvirt-devel >= 0.6.1.4-5
BuildRequires: lua, lua-devel, perl-devel, perl-generators, perl-macros, perl(Sys::Virt), perl(Test::More), perl(Test::Pod) >= 1.00, perl(Test::Pod::Coverage) >= 1.00
BuildRequires: perl(Module::Build), perl(ExtUtils::CBuilder), perl(Locale::TextDomain), python3-devel
BuildRequires: libvirt-python3, ruby-devel, rubygem-rake, rubygem(json), rubygem(rdoc), rubygem(test-unit), ruby-irb, java-1.8.0-openjdk, java-1.8.0-openjdk-devel
BuildRequires: jpackage-utils, php-devel, gobject-introspection-devel, gjs, acl, attr, augeas-libs, bash, binutils, btrfs-progs, lzop, mdadm, nilfs-utils
BuildRequires: bzip2, coreutils, cpio, cryptsetup, debootstrap, dhclient, diffutils, dosfstools, e2fsprogs, file, findutils, gawk, gdisk, gfs2-utils
BuildRequires: grep, gzip, hivex, iproute, iputils, jfsutils, kmod, kpartx, less, libcap, libldm, libselinux, libxml2, lsof, lsscsi, lvm2, strace
BuildRequires: openssh-clients, parted, pciutils, pcre, policycoreutils, procps, psmisc, qemu-img, reiserfs-utils, rsync, scrub, sed, sleuthkit, squashfs-tools
BuildRequires: systemd, tar, udev, util-linux, vim-minimal, which, xfsprogs, yajl, zerofree, hfsplus-tools, ntfs-3g, ntfsprogs gettext-devel binutils
BuildRequires: vala
%ifarch x86_64
BuildRequires: syslinux syslinux-extlinux
%endif
Requires:      supermin >= 5.1.18, augeas-libs%{?_isa} >= 1.7.0, libacl%{?_isa}, libcap%{?_isa}, hivex%{?_isa}, pcre%{?_isa}, libselinux%{?_isa}, systemd-libs%{?_isa}
Requires:      yajl%{?_isa}, libdb-utils, fuse, /usr/bin/qemu-img, libvirt-daemon-kvm >= 0.10.2-3, selinux-policy >= 3.11.1-63, bundled(gnulib), /usr/bin/hexedit, binutils
Requires:      /usr/bin/less, /usr/bin/vi, gnupg2, xz, curl, perl(Sys::Virt),  gawk, gzip, unzip, libvirt
Suggests:      osinfo-db
Recommends:    libguestfs-xfs, nbdkit, nbdkit-plugin-python3, nbdkit-plugin-vddk
Conflicts:     libguestfs-winsupport
%ifarch aarch64 x86_64
Provides:      %{name}-benchmarking%{?_isa} %{name}-benchmarking
Obsoletes:     %{name}-benchmarking < %{version}-%{release}
%endif
Provides:      %{name}-forensics%{?_isa} %{name}-forensics
Obsoletes:     %{name}-forensics < %{version}-%{release}
Provides:      %{name}-gfs2%{?_isa} %{name}-gfs2
Obsoletes:     %{name}-gfs2 < %{version}-%{release}
Provides:      %{name}-hfsplus%{?_isa} %{name}-hfsplus
Obsoletes:     %{name}-hfsplus < %{version}-%{release}
Provides:      %{name}-jfs%{?_isa} %{name}-jfs
Obsoletes:     %{name}-jfs < %{version}-%{release}
Provides:      %{name}-nilfs%{?_isa} %{name}-nilfs
Obsoletes:     %{name}-nilfs < %{version}-%{release}
Provides:      %{name}-reiserfs%{?_isa} %{name}-reiserfs
Obsoletes:     %{name}-reiserfs < %{version}-%{release}
Provides:      %{name}-rsync%{?_isa} %{name}-rsync
Obsoletes:     %{name}-rsync < %{version}-%{release}
Provides:      %{name}-rescue%{?_isa} %{name}-rescue
Obsoletes:     %{name}-rescue < %{version}-%{release}
Provides:      %{name}-ufs%{?_isa} %{name}-ufs
Obsoletes:     %{name}-ufs < %{version}-%{release}
Provides:      %{name}-xfs%{?_isa} %{name}-xfs
Obsoletes:     %{name}-xfs < %{version}-%{release}
Provides:      %{name}-tools-c%{?_isa} %{name}-tools-c
Obsoletes:     %{name}-tools-c < %{version}-%{release}
Provides:      %{name}-tools%{?_isa} %{name}-tools
Obsoletes:     %{name}-tools < %{version}-%{release}
Provides:      virt-dib%{?_isa} virt-dib
Obsoletes:     virt-dib < %{version}-%{release}
Provides:      virt-v2v%{?_isa} virt-v2v
Obsoletes:     virt-v2v < %{version}-%{release}
Provides:      virt-p2v-maker%{?_isa} virt-p2v-maker
Obsoletes:     virt-p2v-maker < %{version}-%{release}
Provides:      %{name}-bash-completion%{?_isa} %{name}-bash-completion
Obsoletes:     %{name}-bash-completion < %{version}-%{release}

%description
libguestfs is a set of tools for accessing and modifying virtual machine (VM) disk images.
You can use this for viewing and editing files inside guests, scripting changes to VMs,
monitoring disk used/free statistics, creating guests, P2V, V2V, performing backups, cloning VMs,
building VMs, formatting disks, resizing disks, and much more.
libguestfs can access almost any disk image imaginable. It can do it securely — without needing
root and with multiple layers of defence against rogue disk images. It can access disk images
on remote machines or on CDs/USB sticks. It can access proprietary systems like VMware and Hyper-V.
All this functionality is available through a scriptable shell called guestfish, or an interactive
rescue shell virt-rescue.
libguestfs is a C library that can be linked with C and C++ management programs and has bindings for
about a dozen other programming languages. Using our FUSE module you can also mount guest filesystems
on the host.
The hivex subproject lets you merge changes into the Windows Registry in Windows guests. You can
examine unknown disk images to find out what they contain.
libguestfs has been in continuous development since 2009, with a 250 page manual, deployed in
enterprise environments, and with many happy and successful users.
Dozens of projects are using libguestfs today.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}, pkgconfig, xz

%description devel
This package includes development files for %{name}.

%package -n ocaml-%{name}
Summary:       Ocaml bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description -n ocaml-%{name}
This package includes ocaml bindings for %{name}.

%package -n ocaml-%{name}-devel
Summary:       Development files of ocaml bindings for %{name}
Requires:      ocaml-%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description -n ocaml-%{name}-devel
This package includes development files of ocaml bindings for %{name}.

%package -n perl-Sys-Guestfs
Summary:       Perl bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}, perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-Sys-Guestfs
This package includes perl bindings for %{name}.

%package -n python3-%{name}
Summary:       Python 3 bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package includes python 3 bindings for %{name}.

%package -n ruby-%{name}
Summary:       Ruby bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}, ruby(release), ruby
Provides:      ruby(guestfs) = %{version}

%description -n ruby-%{name}
This package includes ruby bindings for %{name}.

%package -n php-%{name}
Summary:       PHP bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}, php(zend-abi) = %{php_zend_api}, php(api) = %{php_core_api}

%description -n php-%{name}
This package includes PHP bindings for %{name}.

%package -n lua-guestfs
Summary:       Lua bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}, lua

%description -n lua-guestfs
This package includes lua bindings for %{name}.

%package gobject
Summary:       GObject bindings for %{name}
Requires:      %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description gobject
This package includes GObject bindings for %{name}.

%package gobject-devel
Summary:       Development files of GObject bindings for %{name}
Requires:      %{name}-gobject = %{epoch}:%{version}-%{release}

%description gobject-devel
This package includes development files of GOBject bindings for %{name}.

%package vala
Summary:       Vala for %{name}
Requires:      %{name}-devel
Requires:      vala

%description vala
This package contains Vala bindings for %{name}.

%package       help
Summary:       man files for %{name}
Requires:      man
Provides:      %{name}-man-pages-ja%{?_isa} %{name}-man-pages-ja
Obsoletes:     %{name}-man-pages-ja < %{version}-%{release}
Provides:      %{name}-man-pages-uk%{?_isa} %{name}-man-pages-uk
Obsoletes:     %{name}-man-pages-uk < %{version}-%{release}

%description   help
This package includes man files for %{name}.

%prep
%autosetup -p1

cd ..
cp -a %{name}-%{version} %{name}-%{version}-python3
cd -

if [ "$(stat -f -L -c %T .)" != "nfs" ] && [ "$(getenforce | tr '[A-Z]' '[a-z]')" != "disabled" ]; then
    chcon --reference=/tmp tmp
fi

sed -i 's/FEDORA | RHEL | CENTOS)/FEDORA | RHEL | CENTOS | OPENEULER | GENERIC)/g' configure

%build
ip addr list ||:
ip route list ||:
if ping -c 3 -w 20 8.8.8.8; then
  extra=
else
  mkdir cachedir repo
  findres=`find /var/cache/dnf -type f -name '*.rpm' -print0`
if [ ! -z "$findres"]; then
  echo $find_res | xargs -0 -n 1 cp -t repo
fi
  createrepo repo
  sed -e "s|@PWD@|$(pwd)|" %{SOURCE2} > yum.conf
  extra=--with-supermin-packager-config=$(pwd)/yum.conf
fi

%global localconfigure \
  %{configure} \\\
    --with-default-backend=libvirt \\\
    --with-extra="libvirt" \\\
    --without-java \\\
    $extra
%global localconfigure %{localconfigure} --disable-golang

%global localmake \
  %make_build \
  %make_build V=1 INSTALLDIRS=vendor

%{localconfigure}
%{localmake}

cd ../%{name}-%{version}-python3
export PYTHON=%{__python3}
while [ ! -f ../%{name}-%{version}/generator/.pod2text* ]
do
  sleep 1
done     
cp ../%{name}-%{version}/generator/.pod2text* generator/
%{localconfigure} --enable-python --enable-perl --disable-ruby --disable-haskell --disable-php --disable-erlang --disable-lua --disable-golang --disable-gobject
%{localmake}
cd -
wait

%check

%install

%make_install INSTALLDIRS=vendor NO_PACKLIST=1

cd ../%{name}-%{version}-python3
%make_install INSTALLDIRS=vendor -C python
cd -

rm $( find $RPM_BUILD_ROOT -name '*.a' | grep -v /ocaml/ )

find $RPM_BUILD_ROOT -name '*.la' -delete

find $RPM_BUILD_ROOT -name perllocal.pod -delete
find $RPM_BUILD_ROOT -name '*.bs' -delete
find $RPM_BUILD_ROOT -name 'bindtests.pl' -delete

install -d $RPM_BUILD_ROOT%{_libdir}/guestfs
install -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

rm -rf $RPM_BUILD_ROOT%{_libdir}/ocaml/v2v_test_harness
rm -rf $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllv2v_test_harness*

rm -rf ocaml/html/.gitignore


%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README AUTHORS HACKING examples/*.c 
%{_bindir}/libguestfs-test-tool
%{_bindir}/guest*
%{_bindir}/virt-*
%exclude %{_bindir}/virt-tar*
%{_libdir}/guestfs/
%{_libdir}/libguestfs.so.*
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf
%config %{_sysconfdir}/profile.d/guestfish.sh
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/guest*
%{_datadir}/bash-completion/completions/libguestfs-test-tool
%{_datadir}/bash-completion/completions/virt-*

%files devel
%{_libdir}/libguestfs.so
%{_includedir}/guestfs.h
%{_libdir}/pkgconfig/libguestfs.pc
%{_sbindir}/libguestfs-make-fixed-appliance

%files -n ocaml-%{name}
%{_libdir}/ocaml/guestfs
%exclude %{_libdir}/ocaml/guestfs/*.a
%exclude %{_libdir}/ocaml/guestfs/*.cmxa
%exclude %{_libdir}/ocaml/guestfs/*.cmx
%exclude %{_libdir}/ocaml/guestfs/*.mli
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner

%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml ocaml/html
%{_libdir}/ocaml/guestfs/*.a
%{_libdir}/ocaml/guestfs/*.cmxa
%{_libdir}/ocaml/guestfs/*.cmx
%{_libdir}/ocaml/guestfs/*.mli

%files -n perl-Sys-Guestfs
%doc perl/examples/*.pl
%{perl_vendorarch}/*

%files -n python3-%{name}
%doc python/examples/*.py
%{python3_sitearch}/libguestfsmod*.so
%{python3_sitearch}/guestfs.py
%{python3_sitearch}/__pycache__/guestfs*.py*

%files -n ruby-%{name}
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%{ruby_vendorlibdir}/guestfs.rb
%{ruby_vendorarchdir}/_guestfs.so

%files -n php-%{name}
%doc php/README-PHP
%dir %{_sysconfdir}/php.d
%{_sysconfdir}/php.d/guestfs_php.ini
%{_libdir}/php/modules/guestfs_php.so

%files -n lua-guestfs
%doc lua/examples/*.lua
%doc lua/examples/LICENSE
%{_libdir}/lua/*/guestfs.so

%files gobject
%{_libdir}/libguestfs-gobject-1.0.so.0*
%{_libdir}/girepository-1.0/Guestfs-1.0.typelib

%files gobject-devel
%{_libdir}/libguestfs-gobject-1.0.so
%{_includedir}/guestfs-gobject.h
%dir %{_includedir}/guestfs-gobject
%{_includedir}/guestfs-gobject/*.h
%{_datadir}/gir-1.0/Guestfs-1.0.gir
%{_libdir}/pkgconfig/libguestfs-gobject-1.0.pc

%files vala
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.deps
%{_datadir}/vala/vapi/libguestfs-gobject-1.0.vapi

%files help
%{_mandir}/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(uk) %{_mandir}/uk/man*/*

%changelog
* Wed Feb 22 2023 wulei <wulei80@h-partners.com> - 1:1.49.5-2
- Enable Vala bindings

* Sat Nov 12 2022 dan <fzhang@zhixundn.com> - 1:1.49.5-1
- update to 1.49.5

* Thu May 26 2022 Jun Yang <jun.yang@suse.com> - 1:1.40.2-17
- Remove unnecessary dependency of kernel package

* Tue Apr 19 2022 wangkai <wangkai385@h-partners.com> - 1:1.40.2-16
- Fix build error

* Wed Oct 13 2021 wuzhen <wuzhen36@huawei.com> - 1:1.40.2-15
- Compile two packages in parallel 

* Tue Jul 20 2021 sunguoshuai <sunguoshuai@huawei.com> - 1:1.40.2-14
- No /var/cache/yum in build environment and add test incase no cached rpms.

* Mon Mar 22 2021 lingsheng <lingsheng@huawei.com> - 1:1.40.2-14
- Remove wget check

* Mon Mar 01 2021 maminjie <maminjie1@huawei.com> - 1:1.40.2-13
- Fix php 8.0.0 warning about missing arginfo

* Wed Feb 10 2021 baizhonggui <baizhonggui@huawei.com> - 1:1.40.2-12
- Delete python2 subpackage

* Thu Dec 31 2020 maminjie <maminjie1@huawei.com> - 1:1.40.2-11
- Port to php 8.0.0

* Wed Dec 16 2020 maminjie <maminjie1@huawei.com> - 1:1.40.2-10
- Enable appliance that is necessary

* Tue Jul 21 2020 sunguoshuai <sunguoshuai@huawei.com> - 1:1.40.2-9
- Del the optimization for xfs, which can lead to du and find command aborted.

* Sat Jun 20 2020 chengzihan <chengzihan2@huawei.com> - 1:1.40.2-8
- fix the problem: PYTHON_LIBS is not set in Python 3.8
- and add BuildRequires: gettext-devel
- delete BuildRequires: python2-libvirt, which is no longer provided

* Fri May 29 2020 lizhenhua <lizhenhua21@huawei.com> - 1:1.40.2-7
- Disable appliance

* Tue Mar 10 2020 yangjian<yangjian79@huawei.com> - 1:1.40.2-6
- Type:NA
- ID:NA
- SUG:NA
- DESC: Change Source to available address

* Mon Mar 9 2020 hy <eulerstoragemt@huawei.com> - 1:1.39.8-5
- Type:NA
- ID:NA
- SUG:NA
- DESC: delete the unused require mingw32-srvany

* Sat Mar 7 2020 hy <eulerstoragemt@huawei.com> - 1:1.39.8-4
- Type:NA
- ID:NA
- SUG:NA
- DESC:Remove Java bingdings, zz-packages-zfs command and rhsrvany.exe from mingw32-srvany.

* Mon Dec 16 2019 zoujing<zoujing13@huawei.com> - 1:1.39.8-3
- Type:NA
- ID:NA
- SUG:NA
- DESC:fix install problem

* Sat Nov 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:1.39.8-2
- Package init
