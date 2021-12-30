%define oname terminal

Name:           cutefish-terminal
Version:        0.7
Release:        1
Summary:        Simple terminal
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/cutefishos/terminal
Source:         https://github.com/cutefishos/terminal/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  cmake
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
A simple terminal based on QMLTermWidget.


%prep
%autosetup -n %{oname}-%{version} -p1
sed -i 's/\(Name=\)\(Terminal\)/\1Cutefish \2/' %{name}.desktop

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/qt5/qml/Cutefish/TermWidget/
