Name:		booth
Version:	1.1.3~20250205
Release:	1
Summary:	Maui Camera App
URL:    	https://invent.kde.org/maui/booth
Source0:	https://invent.kde.org/maui/booth/-/archive/v%{version}/maui-booth-v%{version}.tar.bz2
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

%description
Maui Camera App
Booth is a convergent camera app, to record videos and take pictures and sync your cmera photos.

%prep
%autosetup -p1 -n maui-%{name}-v%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang booth

%files -f booth.lang
%{_bindir}/booth
%{_datadir}/applications/org.kde.booth.desktop
%{_datadir}/metainfo/org.kde.booth.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/booth.svg
