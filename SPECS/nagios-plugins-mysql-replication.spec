%define debug_package %{nil}

Summary:	A plugin for nagios that will check the status of MySQL replication
Name:		nagios-plugins-mysql-replication
Version:	1.1
Release:	3%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		http://thesharp.ru/nagios-plugins/
Source0:	http://thesharp.ru/nagios-plugins/mysql-replication/nagios-plugins-mysql-replication-%{version}.tar.gz
Requires:	nagios-plugins, mysql
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A plugin for nagios that will check the status of MySQL replication.

%prep
%setup -q -n nagios-plugins-mysql-replication-%{version}
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" check_mysql_replication

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 check_mysql_replication %{buildroot}%{_libdir}/nagios/plugins/check_mysql_replication
install -D -p -m 0644 mysql-replication.cfg %{buildroot}%{_sysconfdir}/nagios/mysql-replication.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog README
%{_libdir}/nagios/plugins/check_mysql_replication
%config(noreplace) %{_sysconfdir}/nagios/mysql-replication.cfg

%changelog
* Sun Sep 18 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-3.vortex
- Remove dot from summary.

* Thu Sep  8 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-2.vortex
- Vortex rebranding.

* Tue Aug  9 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-1
- Initial packaging for CentOS.

