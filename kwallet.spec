%define major 5
%define libname %mklibname KF5Wallet %{major}
%define devname %mklibname KF5Wallet -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kwallet
Version: 5.116.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/kwallet-%{version}.tar.xz
Summary: The KDE Frameworks 5 password storage library
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(Qca-qt5)
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
BuildRequires: %{_lib}assuan-devel
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
%rename kwallet5
Recommends: kwalletd
Recommends: kwallet-query

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1 -n kwallet-%{version}
# We get kwalletd and kwallet-query from kf6-kwallet
%cmake_kde5 \
	-DBUILD_KWALLETD:BOOL=OFF \
	-DBUILD_KWALLET_QUERY:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build
# We don't need translations for components that are
# now disabled (kwalletd and kwallet-query), and those
# are the only translations shipped with kwallet
rm -rf %{buildroot}%{_datadir}/locale

%files
%{_datadir}/dbus-1/*/*
%{_datadir}/qlogging-categories5/kwallet.*categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Wallet
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
