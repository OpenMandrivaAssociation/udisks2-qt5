%global debug_package %{nil}

%define major		0
%define libname		%mklibname %{name}_ %{major}
%define develname	%mklibname %{name} -d

Name:		udisks2-qt5
Version:	5.0.6
Release:	2
Summary:	Package provides Qt5 binding for udisks2
Group:		System/Libraries
License:	GPLv3+
URL:		https://github.com/linuxdeepin/udisks2-qt5
Source0:	https://github.com/linuxdeepin/udisks2-qt5/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  qmake5
BuildRequires:  qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)

%description
This package provides a Qt5 binding for udisks2.

#------------------------------------------------

%package -n	%{libname}
Summary:	Qt5 library for udisks2
Group:		System/Libraries
Obsoletes:	%{_lib}udisks2-qt50 < 0.0.1-2

%description -n	%{libname}
This package provides a Qt5 binding for udisks2.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup

sed -i 's|/lib|/%{_lib}|' udisks2.pro

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files -n %{libname}
%doc CHANGELOG.md
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
