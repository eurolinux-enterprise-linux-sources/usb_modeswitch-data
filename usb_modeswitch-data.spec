%global source_name	usb-modeswitch-data

Name:		usb_modeswitch-data
Version:	20170806
Release:	1%{?dist}
Summary:	USB Modeswitch gets mobile broadband cards in operational mode
Summary(de):	USB Modeswitch aktiviert UMTS-Karten
Group:		Applications/System
License:	GPLv2+
URL:		http://www.draisberghof.de/usb_modeswitch/
Source0:	http://www.draisberghof.de/usb_modeswitch/%{source_name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	systemd
Requires:	systemd
Requires:	usb_modeswitch >= 2.4.0


%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-devices and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to function.

%description	-l de
USB Modeswitch deaktiviert die CDROM-Emulation einiger UMTS-Karten.
Dadurch erkennt Linux die Datenkarte und kann damit Internet-
Verbindungen aufbauen. Die gängigen Karten von Huawei, T-Mobile,
Vodafone, Option, ZTE und Novatell werden unterstützt.

Dieses Paket enthält die Dateien für usb_modeswitch benötigt 
um zu funktionieren.


%prep
%setup -q -n %{source_name}-%{version}

%build

%install
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	RULESDIR=$RPM_BUILD_ROOT%{_udevrulesdir}

%post 
%udev_rules_update

%postun
%udev_rules_update

%files
%{_udevrulesdir}/40-usb_modeswitch.rules
%{_datadir}/usb_modeswitch
%license COPYING
%doc ChangeLog README REFERENCE

%changelog
* Tue Aug 29 2017 Lubomir Rintel <lrintel@redhat.com> - 20170806-1
- Update to a new release (rh #1483051)

* Thu Jul 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 20160612-2
- Install the rules into proper location (rh #1352055)
- Bring back the module binding

* Wed Jun 22 2016 Lubomir Rintel <lkundrak@v3.sk> - 20160612-1
- Update to a new release

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20130807-2
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Dan Williams <dcbw@redhat.com> - 20130807-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130610-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 20130610-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 20121109-1
- New upstream release. Resolves rhbz#875833

* Fri Aug 24 2012 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 20120815-1
- New upstream release. Resolves rhbz#847681

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Dan Williams <dcbw@redhat.com> 20120531-1
- New upstream data release
- Handle failure of udevadm control --reload-rules (rh #824849)

* Tue Apr 24 2012 Dan Williams <dcbw@redhat.com> 20120120-1
- New upstream release.
- Remove dep on TCL since nothing in the package requires it

* Tue Oct 25 2011 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20111023-1
- New upstream release.

* Mon Jul 25 2011 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20110714-1
- New upstream release. Resolves rhbz#714648

* Mon Mar 28 2011 Rahul Sundaram <sundaram@fedoraproject.org> 20110227-1
- New upstream release.  Resolves rhbz#654800
- Update spec to match current guidelines
- Some spec file fixes from Alexander Todorov. Resolves rhbz#632559
- Drop patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Dan Williams <dcbw@redhat.com> 20101222-1
- New upstream

* Tue Aug 24 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20100817-1
- New upstream

* Thu Aug 12 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20100707-1
- New upstream

* Tue Jun 22 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20100621-1
- New upstream

* Tue Apr 20 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20100418-2
- Remove buildroot, make package noarch

* Tue Apr 20 2010 Huzaifa Sidhpurwala <huzaifas@redhat.com> 20100418-1
- First build
