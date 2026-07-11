%global tl_name stealcaps
%global tl_revision 64967

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Steal small capitals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stealcaps
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stealcaps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This little package is mainly meant to be used when there is a (TrueType
or OpenType) font that does not provide real small capitals. As a
workaround, this package helps to borrow, or "steal", the small capitals
from another font. This might also be useful in the rare case that
someone does not like the present small capitals, and wants to change
them, or likes those from another font better. To achieve the borrowing,
one only needs to load the package and specify the name of the target
font via the from option. Package dependencies: pgfopts, iftex,
fontspec.

