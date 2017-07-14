Name     : pcre
Version  : 8.41
Release  : 41
URL      : https://github.com/svn2github/pcre/archive/master.zip
Source0  : https://github.com/svn2github/pcre/archive/master.zip
Summary  : PCREPosix - Posix compatible interface to libpcre
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcre-bin
Requires: pcre-lib
Requires: pcre-doc
BuildRequires : bzip2-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
-----------------------------------------------------------------
NOTE: This set of files relates to PCRE releases that use the original API,
with library names libpcre, libpcre16, and libpcre32. January 2015 saw the
first release of a new API, known as PCRE2, with release numbers starting at
10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old
libraries (now called PCRE1) are still being maintained for bug fixes, but
there will be no new development. New projects are advised to use the new PCRE2
libraries.

%package bin
Summary: bin components for the pcre package.
Group: Binaries

%description bin
bin components for the pcre package.


%package dev
Summary: dev components for the pcre package.
Group: Development
Requires: pcre-lib
Requires: pcre-bin
Provides: pcre-devel

%description dev
dev components for the pcre package.


%package dev32
Summary: dev32 components for the pcre package.
Group: Default
Requires: pcre-lib32
Requires: pcre-bin
Requires: pcre-dev

%description dev32
dev32 components for the pcre package.


%package doc
Summary: doc components for the pcre package.
Group: Documentation

%description doc
doc components for the pcre package.


%package extras
Summary: extras components for the pcre package.
Group: Default

%description extras
extras components for the pcre package.


%package lib
Summary: lib components for the pcre package.
Group: Libraries

%description lib
lib components for the pcre package.


%package lib32
Summary: lib32 components for the pcre package.
Group: Default

%description lib32
lib32 components for the pcre package.


%prep
%setup -q -n pcre-master
pushd ..
cp -a pcre-master build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491245017
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%autogen --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check ; ./RunTest

%install
export SOURCE_DATE_EPOCH=1491245017
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcre-config
/usr/bin/pcregrep
/usr/bin/pcretest

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libpcre.so
/usr/lib64/libpcre16.so
/usr/lib64/libpcre32.so
/usr/lib64/libpcrecpp.so
/usr/lib64/libpcreposix.so
/usr/lib64/pkgconfig/libpcre.pc
/usr/lib64/pkgconfig/libpcre16.pc
/usr/lib64/pkgconfig/libpcre32.pc
/usr/lib64/pkgconfig/libpcrecpp.pc
/usr/lib64/pkgconfig/libpcreposix.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so
/usr/lib32/libpcre16.so
/usr/lib32/libpcre32.so
/usr/lib32/libpcrecpp.so
/usr/lib32/libpcreposix.so
/usr/lib32/pkgconfig/32libpcre.pc
/usr/lib32/pkgconfig/32libpcre16.pc
/usr/lib32/pkgconfig/32libpcre32.pc
/usr/lib32/pkgconfig/32libpcrecpp.pc
/usr/lib32/pkgconfig/32libpcreposix.pc
/usr/lib32/pkgconfig/libpcre.pc
/usr/lib32/pkgconfig/libpcre16.pc
/usr/lib32/pkgconfig/libpcre32.pc
/usr/lib32/pkgconfig/libpcrecpp.pc
/usr/lib32/pkgconfig/libpcreposix.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/pcre/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/libpcrecpp.so.0
/usr/lib64/libpcrecpp.so.0.0.1

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libpcrecpp.so.0
%exclude /usr/lib64/libpcrecpp.so.0.0.1
/usr/lib64/libpcre.so.1
/usr/lib64/libpcre.so.1.2.8
/usr/lib64/libpcre16.so.0
/usr/lib64/libpcre16.so.0.2.8
/usr/lib64/libpcre32.so.0
/usr/lib64/libpcre32.so.0.0.8
/usr/lib64/libpcreposix.so.0
/usr/lib64/libpcreposix.so.0.0.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so.1
/usr/lib32/libpcre.so.1.2.8
/usr/lib32/libpcre16.so.0
/usr/lib32/libpcre16.so.0.2.8
/usr/lib32/libpcre32.so.0
/usr/lib32/libpcre32.so.0.0.8
/usr/lib32/libpcrecpp.so.0
/usr/lib32/libpcrecpp.so.0.0.1
/usr/lib32/libpcreposix.so.0
/usr/lib32/libpcreposix.so.0.0.4
