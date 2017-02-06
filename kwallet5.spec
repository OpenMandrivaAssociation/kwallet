%define major 5
%define libname %mklibname KF5Wallet %{major}
%define devname %mklibname KF5Wallet -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet5
Version: 5.31.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/kwallet-%{version}.tar.xz
Summary: The KDE Frameworks 5 password storage library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
%if %mdvver >= 3000000
# FIXME should do the right thing here:
#BuildRequires: cmake(Gpgmepp)
#BuildRequires: cmake(QGpgme)
# But currently there's conflicts because kdepimlibs4-devel provides
# cmake(QGpgme) as well and lib64GpgMePp5 vs. lib64gpgmepp6 confusion
BuildRequires: %{_lib}gpgme-devel >= 1.8.0-2
BuildRequires: %{_lib}gpgmepp-devel >= 1.8.0-2
BuildRequires: %{_lib}qgpgme-devel >= 1.8.0-2
%else
BuildRequires: cmake(KF5Gpgmepp)
%endif
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: boost-devel
Requires: %{libname} = %{EVRD}

%description
KWallet is an abstraction to password storage.

%package -n %{libname}
Summary: The KDE Frameworks 5 password storage library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KWallet is an abstraction to password storage.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
KWallet is an abstraction to password storage.

%prep
%setup -q -n kwallet-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kwalletd5
%find_lang kwallet-query

%files -f kwalletd5.lang,kwallet-query.lang
%{_bindir}/kwalletd%{major}
%{_bindir}/kwallet-query
%{_datadir}/dbus-1/*/*
%{_datadir}/knotifications5/*
%{_datadir}/kservices5/*
%{_mandir}/man1/kwallet-query.1.*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Wallet
%{_libdir}/qt5/mkspecs/modules/*
