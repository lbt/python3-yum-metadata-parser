Name:       python3-yum-metadata-parser
Summary:    YUM metadata parser written in C.
Version:    1.1.1
Release:    1
License:    LGPL v2.1
URL:        https://github.com/rpm-software-management/yum-metadata-parser
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)

%description
The rpm yum-metadata-parser module is used by yum

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
