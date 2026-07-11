%global tl_name chemplants
%global tl_revision 60606

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.9
Release:	%{tl_revision}.1
Summary:	Symbology to draw chemical plants with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/chemplants
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemplants.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemplants.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers tools to draw simple or barely complex schemes of
chemical processes. The package defines several standard symbols and
styles to draw process units and streams. The guiding light of the
package is the UNICHIM regulation. All of the symbols and styles are
defined using tools of the TikZ package, thus a basic knowledge of the
logic of this powerful tool is required to profitably use chemplants.

