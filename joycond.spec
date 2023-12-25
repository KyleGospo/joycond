Name:           joycond
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Nintendo Switch Pro and Joycon pairing Daemon

License:        GPL-3.0 license
URL:            https://github.com/KyleGospo/joycond
VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}

BuildRequires:  cmake, gcc, gcc-c++, libevdev-devel, libudev-devel
Requires:       libevdev-devel, libudev-devel

%description
joycond is a linux daemon which uses the evdev devices provided by hid-nintendo (formerly known as hid-joycon) to implement joycon pairing.

%prep
{{{ git_dir_setup_macro }}}

%build
cmake .
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_exec_prefix}/lib/udev/rules.d/
install -m644 %{buildroot}/lib/udev/rules.d/89-joycond.rules %{buildroot}%{_exec_prefix}/lib/udev/rules.d/89-joycond.rules
install -m644 %{buildroot}/lib/udev/rules.d/72-joycond.rules %{buildroot}%{_exec_prefix}/lib/udev/rules.d/72-joycond.rules
rm -R %{buildroot}/lib/udev/rules.d/

%files
%{_sysconfdir}/modules-load.d/joycond.conf
%{_sysconfdir}/systemd/system/joycond.service
%{_exec_prefix}/lib/udev/rules.d/*
%{_bindir}/joycond

%changelog
{{{ git_dir_changelog }}}
