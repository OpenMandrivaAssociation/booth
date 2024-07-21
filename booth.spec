Name:		booth
Version:	1.1.1
Release:	1
Summary:	Maui Camera App
URL:    	https://invent.kde.org/maui/booth
Source0:	https://invent.kde.org/maui/booth/-/archive/v%{version}/booth-v%{version}.tar.bz2
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

%description
Maui Camera App
Booth is a convergent camera app, to record videos and take pictures and sync your cmera photos.

%prep
%autosetup -p1 -n %{name}-v%{version}
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
