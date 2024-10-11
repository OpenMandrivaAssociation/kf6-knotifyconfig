%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6NotifyConfig
%define devname %mklibname KF6NotifyConfig -d
#define git 20240217

Name: kf6-knotifyconfig
Version: 6.7.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/knotifyconfig/-/archive/master/knotifyconfig-master.tar.bz2#/knotifyconfig-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/knotifyconfig-%{version}.tar.xz
%endif
Summary: Configuration dialog for desktop notifications
URL: https://invent.kde.org/frameworks/knotifyconfig
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: pkgconfig(libcanberra)
Requires: %{libname} = %{EVRD}

%description
Configuration dialog for desktop notifications

%package -n %{libname}
Summary: Configuration dialog for desktop notifications
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Configuration dialog for desktop notifications

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Configuration dialog for desktop notifications

%prep
%autosetup -p1 -n knotifyconfig-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/knotifyconfig.*

%files -n %{devname}
%{_includedir}/KF6/KNotifyConfig
%{_libdir}/cmake/KF6NotifyConfig
%{_qtdir}/doc/KF6NotifyConfig.*

%files -n %{libname}
%{_libdir}/libKF6NotifyConfig.so*
