#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x9766E084FB0F43D8 (ph10@cam.ac.uk)
#
Name     : pcre
Version  : 8.45
Release  : 76
URL      : https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz
Source0  : https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz
Source1  : https://sourceforge.net/projects/pcre/files/pcre/8.45/pcre-8.45.tar.gz.sig
Summary  : PCRE - Perl compatible regular expressions C library with 8 bit character support
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-license = %{version}-%{release}
Requires: pcre-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
-----------------------------------------------------------------
NOTE: This set of files relates to PCRE releases that use the original API,
with library names libpcre, libpcre16, and libpcre32. January 2015 saw the
first release of a new API, known as PCRE2, with release numbers starting at
10.00 and library names libpcre2-8, libpcre2-16, and libpcre2-32. The old
libraries (now called PCRE1) are now at end of life, and 8.45 is the final
release. New projects are advised to use the new PCRE2 libraries.

%package bin
Summary: bin components for the pcre package.
Group: Binaries
Requires: pcre-license = %{version}-%{release}

%description bin
bin components for the pcre package.


%package dev
Summary: dev components for the pcre package.
Group: Development
Requires: pcre-lib = %{version}-%{release}
Requires: pcre-bin = %{version}-%{release}
Provides: pcre-devel = %{version}-%{release}
Requires: pcre = %{version}-%{release}

%description dev
dev components for the pcre package.


%package dev32
Summary: dev32 components for the pcre package.
Group: Default
Requires: pcre-lib32 = %{version}-%{release}
Requires: pcre-bin = %{version}-%{release}
Requires: pcre-dev = %{version}-%{release}

%description dev32
dev32 components for the pcre package.


%package doc
Summary: doc components for the pcre package.
Group: Documentation
Requires: pcre-man = %{version}-%{release}

%description doc
doc components for the pcre package.


%package extras
Summary: extras components for the pcre package.
Group: Default

%description extras
extras components for the pcre package.


%package extras-unicode
Summary: extras-unicode components for the pcre package.
Group: Default

%description extras-unicode
extras-unicode components for the pcre package.


%package lib
Summary: lib components for the pcre package.
Group: Libraries
Requires: pcre-license = %{version}-%{release}

%description lib
lib components for the pcre package.


%package lib32
Summary: lib32 components for the pcre package.
Group: Default
Requires: pcre-license = %{version}-%{release}

%description lib32
lib32 components for the pcre package.


%package license
Summary: license components for the pcre package.
Group: Default

%description license
license components for the pcre package.


%package man
Summary: man components for the pcre package.
Group: Default

%description man
man components for the pcre package.


%prep
%setup -q -n pcre-8.45
cd %{_builddir}/pcre-8.45
pushd ..
cp -a pcre-8.45 build32
popd
pushd ..
cp -a pcre-8.45 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683127714
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-jit --enable-utf  --enable-unicode-properties --enable-pcre16 --enable-pcre32
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1683127714
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcre
cp %{_builddir}/pcre-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/pcre/936db4f914d8b9a516ac93a3bf7856c8bfeb6855 || :
cp %{_builddir}/pcre-%{version}/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/pcre/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pcregrep
/V3/usr/bin/pcretest
/usr/bin/pcre-config
/usr/bin/pcregrep
/usr/bin/pcretest

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libpcre.so
/V3/usr/lib64/libpcre16.so
/V3/usr/lib64/libpcre32.so
/V3/usr/lib64/libpcrecpp.so
/V3/usr/lib64/libpcreposix.so
/usr/include/pcre.h
/usr/include/pcre_scanner.h
/usr/include/pcre_stringpiece.h
/usr/include/pcrecpp.h
/usr/include/pcrecpparg.h
/usr/include/pcreposix.h
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
/usr/share/man/man3/pcre.3
/usr/share/man/man3/pcre16.3
/usr/share/man/man3/pcre16_assign_jit_stack.3
/usr/share/man/man3/pcre16_compile.3
/usr/share/man/man3/pcre16_compile2.3
/usr/share/man/man3/pcre16_config.3
/usr/share/man/man3/pcre16_copy_named_substring.3
/usr/share/man/man3/pcre16_copy_substring.3
/usr/share/man/man3/pcre16_dfa_exec.3
/usr/share/man/man3/pcre16_exec.3
/usr/share/man/man3/pcre16_free_study.3
/usr/share/man/man3/pcre16_free_substring.3
/usr/share/man/man3/pcre16_free_substring_list.3
/usr/share/man/man3/pcre16_fullinfo.3
/usr/share/man/man3/pcre16_get_named_substring.3
/usr/share/man/man3/pcre16_get_stringnumber.3
/usr/share/man/man3/pcre16_get_stringtable_entries.3
/usr/share/man/man3/pcre16_get_substring.3
/usr/share/man/man3/pcre16_get_substring_list.3
/usr/share/man/man3/pcre16_jit_exec.3
/usr/share/man/man3/pcre16_jit_stack_alloc.3
/usr/share/man/man3/pcre16_jit_stack_free.3
/usr/share/man/man3/pcre16_maketables.3
/usr/share/man/man3/pcre16_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre16_refcount.3
/usr/share/man/man3/pcre16_study.3
/usr/share/man/man3/pcre16_utf16_to_host_byte_order.3
/usr/share/man/man3/pcre16_version.3
/usr/share/man/man3/pcre32.3
/usr/share/man/man3/pcre32_assign_jit_stack.3
/usr/share/man/man3/pcre32_compile.3
/usr/share/man/man3/pcre32_compile2.3
/usr/share/man/man3/pcre32_config.3
/usr/share/man/man3/pcre32_copy_named_substring.3
/usr/share/man/man3/pcre32_copy_substring.3
/usr/share/man/man3/pcre32_dfa_exec.3
/usr/share/man/man3/pcre32_exec.3
/usr/share/man/man3/pcre32_free_study.3
/usr/share/man/man3/pcre32_free_substring.3
/usr/share/man/man3/pcre32_free_substring_list.3
/usr/share/man/man3/pcre32_fullinfo.3
/usr/share/man/man3/pcre32_get_named_substring.3
/usr/share/man/man3/pcre32_get_stringnumber.3
/usr/share/man/man3/pcre32_get_stringtable_entries.3
/usr/share/man/man3/pcre32_get_substring.3
/usr/share/man/man3/pcre32_get_substring_list.3
/usr/share/man/man3/pcre32_jit_exec.3
/usr/share/man/man3/pcre32_jit_stack_alloc.3
/usr/share/man/man3/pcre32_jit_stack_free.3
/usr/share/man/man3/pcre32_maketables.3
/usr/share/man/man3/pcre32_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre32_refcount.3
/usr/share/man/man3/pcre32_study.3
/usr/share/man/man3/pcre32_utf32_to_host_byte_order.3
/usr/share/man/man3/pcre32_version.3
/usr/share/man/man3/pcre_assign_jit_stack.3
/usr/share/man/man3/pcre_compile.3
/usr/share/man/man3/pcre_compile2.3
/usr/share/man/man3/pcre_config.3
/usr/share/man/man3/pcre_copy_named_substring.3
/usr/share/man/man3/pcre_copy_substring.3
/usr/share/man/man3/pcre_dfa_exec.3
/usr/share/man/man3/pcre_exec.3
/usr/share/man/man3/pcre_free_study.3
/usr/share/man/man3/pcre_free_substring.3
/usr/share/man/man3/pcre_free_substring_list.3
/usr/share/man/man3/pcre_fullinfo.3
/usr/share/man/man3/pcre_get_named_substring.3
/usr/share/man/man3/pcre_get_stringnumber.3
/usr/share/man/man3/pcre_get_stringtable_entries.3
/usr/share/man/man3/pcre_get_substring.3
/usr/share/man/man3/pcre_get_substring_list.3
/usr/share/man/man3/pcre_jit_exec.3
/usr/share/man/man3/pcre_jit_stack_alloc.3
/usr/share/man/man3/pcre_jit_stack_free.3
/usr/share/man/man3/pcre_maketables.3
/usr/share/man/man3/pcre_pattern_to_host_byte_order.3
/usr/share/man/man3/pcre_refcount.3
/usr/share/man/man3/pcre_study.3
/usr/share/man/man3/pcre_utf16_to_host_byte_order.3
/usr/share/man/man3/pcre_utf32_to_host_byte_order.3
/usr/share/man/man3/pcre_version.3
/usr/share/man/man3/pcreapi.3
/usr/share/man/man3/pcrebuild.3
/usr/share/man/man3/pcrecallout.3
/usr/share/man/man3/pcrecompat.3
/usr/share/man/man3/pcrecpp.3
/usr/share/man/man3/pcredemo.3
/usr/share/man/man3/pcrejit.3
/usr/share/man/man3/pcrelimits.3
/usr/share/man/man3/pcrematching.3
/usr/share/man/man3/pcrepartial.3
/usr/share/man/man3/pcrepattern.3
/usr/share/man/man3/pcreperform.3
/usr/share/man/man3/pcreposix.3
/usr/share/man/man3/pcreprecompile.3
/usr/share/man/man3/pcresample.3
/usr/share/man/man3/pcrestack.3
/usr/share/man/man3/pcresyntax.3
/usr/share/man/man3/pcreunicode.3

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
%defattr(0644,root,root,0755)
/usr/share/doc/pcre/*

%files extras
%defattr(-,root,root,-)
/V3/usr/lib64/libpcrecpp.so.0
/V3/usr/lib64/libpcrecpp.so.0.0.2
/usr/lib64/libpcrecpp.so.0
/usr/lib64/libpcrecpp.so.0.0.2

%files extras-unicode
%defattr(-,root,root,-)
/V3/usr/lib64/libpcre16.so.0
/V3/usr/lib64/libpcre16.so.0.2.13
/V3/usr/lib64/libpcre32.so.0
/V3/usr/lib64/libpcre32.so.0.0.13
/usr/lib64/libpcre16.so.0
/usr/lib64/libpcre16.so.0.2.13
/usr/lib64/libpcre32.so.0
/usr/lib64/libpcre32.so.0.0.13

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpcre.so.1
/V3/usr/lib64/libpcre.so.1.2.13
/V3/usr/lib64/libpcreposix.so.0
/V3/usr/lib64/libpcreposix.so.0.0.7
/usr/lib64/libpcre.so.1
/usr/lib64/libpcre.so.1.2.13
/usr/lib64/libpcreposix.so.0
/usr/lib64/libpcreposix.so.0.0.7

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpcre.so.1
/usr/lib32/libpcre.so.1.2.13
/usr/lib32/libpcre16.so.0
/usr/lib32/libpcre16.so.0.2.13
/usr/lib32/libpcre32.so.0
/usr/lib32/libpcre32.so.0.0.13
/usr/lib32/libpcrecpp.so.0
/usr/lib32/libpcrecpp.so.0.0.2
/usr/lib32/libpcreposix.so.0
/usr/lib32/libpcreposix.so.0.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcre/936db4f914d8b9a516ac93a3bf7856c8bfeb6855
/usr/share/package-licenses/pcre/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre-config.1
/usr/share/man/man1/pcregrep.1
/usr/share/man/man1/pcretest.1
