%define		status		alpha
%define		pearname	VersionControl_Git
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Provides OO interface to handle Git repository
Name:		php-pear-VersionControl_Git
Version:	0.5.0
Release:	1
License:	Apache
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	67c6ca435359e2eeba75a093801ca6af
URL:		http://pear.php.net/package/VersionControl_Git/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	git-core
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VersionControl_Git is a library that provides OO interface to handle
Git repository. You can use Git command via the wrapper class. Some
features are provided by high-featured interface.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/VersionControl_Git/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/VersionControl/Git.php
%{php_pear_dir}/VersionControl/Git
