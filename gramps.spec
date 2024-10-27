#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v16
# autospec commit: b858a2a
#
Name     : gramps
Version  : 5.2.3
Release  : 35
URL      : https://github.com/gramps-project/gramps/archive/v5.2.3/gramps-5.2.3.tar.gz
Source0  : https://github.com/gramps-project/gramps/archive/v5.2.3/gramps-5.2.3.tar.gz
Summary  : Gramps is a genealogy program for Windows, Linux, Apple MacOS and other UNIX-like systems. It helps you track your family tree by allowing you to store, edit, and research genealogical data.
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: gramps-bin = %{version}-%{release}
Requires: gramps-data = %{version}-%{release}
Requires: gramps-license = %{version}-%{release}
Requires: gramps-locales = %{version}-%{release}
Requires: gramps-man = %{version}-%{release}
Requires: gramps-python = %{version}-%{release}
Requires: gramps-python3 = %{version}-%{release}
Requires: osm-gps-map
Requires: pypi(pyicu)
BuildRequires : buildreq-distutils3
BuildRequires : intltool
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains the catalog needed to use the Gramps glade files in glade.

%package bin
Summary: bin components for the gramps package.
Group: Binaries
Requires: gramps-data = %{version}-%{release}
Requires: gramps-license = %{version}-%{release}

%description bin
bin components for the gramps package.


%package data
Summary: data components for the gramps package.
Group: Data

%description data
data components for the gramps package.


%package doc
Summary: doc components for the gramps package.
Group: Documentation
Requires: gramps-man = %{version}-%{release}

%description doc
doc components for the gramps package.


%package license
Summary: license components for the gramps package.
Group: Default

%description license
license components for the gramps package.


%package locales
Summary: locales components for the gramps package.
Group: Default

%description locales
locales components for the gramps package.


%package man
Summary: man components for the gramps package.
Group: Default

%description man
man components for the gramps package.


%package python
Summary: python components for the gramps package.
Group: Default
Requires: gramps-python3 = %{version}-%{release}

%description python
python components for the gramps package.


%package python3
Summary: python3 components for the gramps package.
Group: Default
Requires: python3-core
Provides: pypi(gramps)

%description python3
python3 components for the gramps package.


%prep
%setup -q -n gramps-5.2.3
cd %{_builddir}/gramps-5.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721056092
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gramps
cp %{_builddir}/gramps-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gramps/ae6bd9ea92f856d6c79bff9e349ef6f17eea0426 || :
cp %{_builddir}/gramps-%{version}/help/COPYING-DOCS %{buildroot}/usr/share/package-licenses/gramps/d4e55a4ce45bed3cec6bbe27f09e20473e7b108f || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
%find_lang gramps
## install_append content
# Need to run *just* install
python3 -tt setup.py install --root=%{buildroot}
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gramps

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gramps_project.Gramps.desktop
/usr/share/gramps/authors.xml
/usr/share/gramps/css/Web_Basic-Ash.css
/usr/share/gramps/css/Web_Basic-Blue.css
/usr/share/gramps/css/Web_Basic-Cypress.css
/usr/share/gramps/css/Web_Basic-Lilac.css
/usr/share/gramps/css/Web_Basic-Peach.css
/usr/share/gramps/css/Web_Basic-Spruce.css
/usr/share/gramps/css/Web_Citations-Animated.css
/usr/share/gramps/css/Web_Citations-Outline.css
/usr/share/gramps/css/Web_DropDown-Menus.css
/usr/share/gramps/css/Web_Fade-Menus.css
/usr/share/gramps/css/Web_Horizontal-Menus.css
/usr/share/gramps/css/Web_Mainz.css
/usr/share/gramps/css/Web_Nebraska.css
/usr/share/gramps/css/Web_Print-Default.css
/usr/share/gramps/css/Web_Vertical-Menus.css
/usr/share/gramps/css/Web_Visually.css
/usr/share/gramps/css/ancestortree.css
/usr/share/gramps/css/behaviour.css
/usr/share/gramps/css/jquery.flexbox.css
/usr/share/gramps/css/lightbox.css
/usr/share/gramps/css/lightbox.js
/usr/share/gramps/css/narrative-maps.css
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_10_4f4221_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_20_372806_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_25_675423_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_25_d5ac5d_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_8_261803_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_diamond_8_443113_10x8.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_flat_75_ddd4b0_40x100.png
/usr/share/gramps/css/swanky-purse/images/ui-bg_highlight-hard_65_fee4bd_1x100.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_070603_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_e8e2b5_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_e9cd86_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_efec9f_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_f2ec64_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_f9f2bd_256x240.png
/usr/share/gramps/css/swanky-purse/images/ui-icons_ff7519_256x240.png
/usr/share/gramps/css/swanky-purse/jquery-ui-1.7.2.custom.css
/usr/share/gramps/css/swanky-purse/jquery-ui-1.7.3.custom.css
/usr/share/gramps/gramps.css
/usr/share/gramps/grampsxml.dtd
/usr/share/gramps/grampsxml.rng
/usr/share/gramps/holidays.xml
/usr/share/gramps/images/add-parent-existing-family.png
/usr/share/gramps/images/add.png
/usr/share/gramps/images/bad.png
/usr/share/gramps/images/caution.png
/usr/share/gramps/images/document.png
/usr/share/gramps/images/down.png
/usr/share/gramps/images/good.png
/usr/share/gramps/images/gramps-export.png
/usr/share/gramps/images/gramps-import.png
/usr/share/gramps/images/gramps-parents-add.png
/usr/share/gramps/images/gramps-parents-open.png
/usr/share/gramps/images/gramps-parents.png
/usr/share/gramps/images/gramps-undo-history.png
/usr/share/gramps/images/gramps-url.png
/usr/share/gramps/images/gramps.png
/usr/share/gramps/images/gramps.svg
/usr/share/gramps/images/gtk-remove.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-fixed-zoom.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-free-zoom.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-place-add.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-place-link.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-event.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-family-down.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-family-up.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-family.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-person.png
/usr/share/gramps/images/hicolor/16x16/actions/geo-show-place.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-addon.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-address.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-attribute.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-bookmark-delete.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-bookmark-edit.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-bookmark-new.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-bookmark.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-citation.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-config.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-date-edit.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-date.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-event.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-family.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-fanchart.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-fanchart2way.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-fanchartdesc.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-font-bgcolor.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-font-color.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-font.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-geo.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-gramplet.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-lock.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-media.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-merge.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-notes.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-parents-add.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-parents-open.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-parents.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-pedigree.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-person.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-place.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-preferences.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-relation.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-reports.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-repository.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-source.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-spouse.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tag-new.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tag.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tools.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tree-group.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tree-list.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-tree-select.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-unlock.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-view.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-viewmedia.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-zoom-best-fit.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-zoom-fit-width.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-zoom-in.png
/usr/share/gramps/images/hicolor/16x16/actions/gramps-zoom-out.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-fixed-zoom.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-free-zoom.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-place-add.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-place-link.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-event.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-family-down.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-family-up.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-family.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-person.png
/usr/share/gramps/images/hicolor/22x22/actions/geo-show-place.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-addon.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-address.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-attribute.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-bookmark-delete.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-bookmark-edit.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-bookmark-new.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-bookmark.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-citation.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-config.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-date-edit.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-date.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-event.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-family.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-fanchart.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-fanchart2way.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-fanchartdesc.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-font-bgcolor.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-font-color.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-font.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo-altmap.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo-birth.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo-death.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo-mainmap.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo-marriage.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-geo.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-gramplet.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-lock.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-media.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-merge.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-notes.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-parents-add.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-parents-open.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-parents.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-pedigree.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-person.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-place.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-preferences.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-relation.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-reports.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-repository.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-source.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-spouse.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tag-new.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tag.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tools.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tree-group.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tree-list.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-tree-select.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-unlock.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-view.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-viewmedia.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-zoom-best-fit.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-zoom-fit-width.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-zoom-in.png
/usr/share/gramps/images/hicolor/22x22/actions/gramps-zoom-out.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-fixed-zoom.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-free-zoom.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-place-add.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-place-link.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-event.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-family-down.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-family-up.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-family.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-person.png
/usr/share/gramps/images/hicolor/24x24/actions/geo-show-place.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-addon.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-address.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-attribute.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-bookmark-delete.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-bookmark-edit.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-bookmark-new.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-bookmark.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-citation.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-config.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-date-edit.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-date.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-event.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-family.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-fanchart.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-fanchart2way.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-fanchartdesc.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-font-bgcolor.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-font-color.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-font.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo-altmap.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo-birth.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo-death.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo-mainmap.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo-marriage.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-geo.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-gramplet.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-lock.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-media.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-merge.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-notes.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-parents-add.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-parents-open.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-parents.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-pedigree.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-person.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-place.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-preferences.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-relation.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-reports.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-repository.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-source.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-spouse.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tag-new.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tag.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tools.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tree-group.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tree-list.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-tree-select.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-unlock.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-view.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-viewmedia.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-zoom-best-fit.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-zoom-fit-width.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-zoom-in.png
/usr/share/gramps/images/hicolor/24x24/actions/gramps-zoom-out.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-fixed-zoom.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-free-zoom.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-place-add.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-place-link.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-event.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-family-down.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-family-up.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-family.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-person.png
/usr/share/gramps/images/hicolor/48x48/actions/geo-show-place.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-addon.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-address.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-attribute.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-bookmark-delete.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-bookmark-edit.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-bookmark-new.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-bookmark.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-citation.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-config.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-date-edit.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-date.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-event.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-family.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-fanchart.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-fanchart2way.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-fanchartdesc.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-font-bgcolor.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-font-color.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-font.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo-altmap.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo-birth.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo-death.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo-mainmap.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo-marriage.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-geo.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-gramplet.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-lock.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-media.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-merge.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-notes.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-parents-add.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-parents-open.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-parents.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-pedigree.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-person.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-place.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-preferences.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-relation.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-reports.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-repository.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-source.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-spouse.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tag-new.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tag.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tools.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tree-group.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tree-list.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-tree-select.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-unlock.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-view.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-viewmedia.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-zoom-best-fit.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-zoom-fit-width.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-zoom-in.png
/usr/share/gramps/images/hicolor/48x48/actions/gramps-zoom-out.png
/usr/share/gramps/images/hicolor/scalable/actions/add-parent-existing-family.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-fixed-zoom.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-free-zoom.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-place-add.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-place-link.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-event.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-family-down.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-family-up.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-family.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-person.svg
/usr/share/gramps/images/hicolor/scalable/actions/geo-show-place.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-addon.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-address.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-attribute.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-bookmark-delete.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-bookmark-edit.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-bookmark-new.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-bookmark.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-citation.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-config.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-date-edit.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-date.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-event.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-family.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-fanchart.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-fanchart2way.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-fanchartdesc.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-font-bgcolor.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-font-color.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-font.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo-altmap.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo-birth.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo-death.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo-mainmap.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo-marriage.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-geo.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-gramplet.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-lock.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-media.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-merge.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-notes.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-parents-add.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-parents-open.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-parents.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-pedigree.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-person.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-place.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-preferences.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-relation.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-reports.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-repository.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-source.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-spouse.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tag-new.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tag.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tools.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tree-group.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tree-list.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-tree-select.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-unlock.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-view.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-viewmedia.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-zoom-best-fit.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-zoom-fit-width.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-zoom-in.svg
/usr/share/gramps/images/hicolor/scalable/actions/gramps-zoom-out.svg
/usr/share/gramps/images/image-missing.png
/usr/share/gramps/images/logo.png
/usr/share/gramps/images/next.png
/usr/share/gramps/images/ped24.ico
/usr/share/gramps/images/previous.png
/usr/share/gramps/images/splash.jpg
/usr/share/gramps/images/stock_index_24.png
/usr/share/gramps/images/stock_link.png
/usr/share/gramps/images/stock_new-html.png
/usr/share/gramps/images/stock_notes.png
/usr/share/gramps/images/text-editor.png
/usr/share/gramps/images/up.png
/usr/share/gramps/images/webstuff/Web_Gender_Female.png
/usr/share/gramps/images/webstuff/Web_Gender_Male.png
/usr/share/gramps/images/webstuff/Web_Gender_Other.png
/usr/share/gramps/images/webstuff/Web_Mainz_Bkgd.png
/usr/share/gramps/images/webstuff/Web_Mainz_Header.png
/usr/share/gramps/images/webstuff/Web_Mainz_Mid.png
/usr/share/gramps/images/webstuff/Web_Mainz_MidLight.png
/usr/share/gramps/images/webstuff/blank.gif
/usr/share/gramps/images/webstuff/crosshairs.png
/usr/share/gramps/images/webstuff/favicon.ico
/usr/share/gramps/images/webstuff/favicon2.ico
/usr/share/gramps/images/webstuff/gramps-geo-altmap.png
/usr/share/gramps/images/webstuff/gramps-geo-birth.png
/usr/share/gramps/images/webstuff/gramps-geo-death.png
/usr/share/gramps/images/webstuff/gramps-geo-mainmap.png
/usr/share/gramps/images/webstuff/gramps-geo-marriage.png
/usr/share/gramps/images/webstuff/somerights20.gif
/usr/share/gramps/lds.xml
/usr/share/gramps/papersize.xml
/usr/share/gramps/tips.xml
/usr/share/icons/hicolor/128x128/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/16x16/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/22x22/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/24x24/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/256x256/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/48x48/apps/org.gramps_project.Gramps.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-gedcom.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-geneweb.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-gramps-package.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-gramps-xml.png
/usr/share/icons/hicolor/48x48/mimetypes/application-x-gramps.png
/usr/share/icons/hicolor/scalable/apps/org.gramps_project.Gramps.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-gedcom.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-geneweb.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-gramps-package.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-gramps-xml.svg
/usr/share/icons/hicolor/scalable/mimetypes/application-x-gramps.svg
/usr/share/metainfo/org.gramps_project.Gramps.metainfo.xml
/usr/share/mime-packages/org.gramps_project.Gramps.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gramps/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gramps/ae6bd9ea92f856d6c79bff9e349ef6f17eea0426
/usr/share/package-licenses/gramps/d4e55a4ce45bed3cec6bbe27f09e20473e7b108f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/cs/man1/gramps.1.gz
/usr/share/man/fr/man1/gramps.1.gz
/usr/share/man/man1/gramps.1.gz
/usr/share/man/nl/man1/gramps.1.gz
/usr/share/man/pl/man1/gramps.1.gz
/usr/share/man/pt_BR/man1/gramps.1.gz
/usr/share/man/sv/man1/gramps.1.gz

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f gramps.lang
%defattr(-,root,root,-)

