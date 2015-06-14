%define major 5
%define libname %mklibname KF5Wallet %{major}
%define devname %mklibname KF5Wallet -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet5
Version: 5.11.0
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
BuildRequires: cmake(Qt5Test)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
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

%files -f kwalletd5.lang
%{_bindir}/kwalletd%{major}
%{_datadir}/dbus-1/*/*
%{_datadir}/knotifications5/*
%{_datadir}/kservices5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Wallet
%{_libdir}/qt5/mkspecs/modules/*
