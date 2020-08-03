---
layout: post
title: Translating GEDCOM to YAML
tags:
notebook: Postach.io
---

Personally, I have trouble sustaining interest in geneology, but I have a bucket-load of family members that are interested, and I sometimes work on software projects for people who like it.

Nonetheless, geneology has some technical challenges that are very interesting.  Maintaining the geneological proof standards is difficult.  While many people have come up with different solutions, it's not a properly solved problem yet.  Sharing that information with others in some way that is both trusted and easy is not a solved problem either.  The “gold standard” in this sharing mechanism even today in 2014 is emailing GEDCOM files backed up with some Word documents.

While I certainly look forward to [GEDCOM X](https://github.com/FamilySearch/gedcomx) developing into something respectable, [GEDCOM](https://en.wikipedia.org/wiki/GEDCOM) is the interchange format of today (2014).  Yech.

GEDCOM is an old and ugly format designed that seems to have been designed in order to display well on IBM 80x24 character terminals.  There was never a good reason to do this.  An examplary GEDCOM file looks like this:

```GEDCOM
0 @I25@ INDI
1 NAME Thomas Trask /Wetmore/ Sr
1 SEX M
1 BIRT
2 DATE 13 March 1866
2 PLAC St. Mary's Bay, Digby, Nova Scotia
2 SOUR Social Security application
1 NATU
2 NAME Thomas T. Wetmore
2 DATE 26 October 1888
2 PLAC Norwich, New London, Connecticut
2 AGE 22 years
2 COUR New London County Court of Common Pleas
2 SOUR court record from National Archives
1 OCCU Antiques Dealer
1 DEAT
2 NAME Thomas Trask Wetmore
2 DATE 17 February 1947
2 PLAC New London, New London, Connecticut
2 AGE 80 years, 11 months, 4 days
2 CAUS Heart Attack
2 SOUR New London Death Records
1 FAMC @F11@
1 FAMS @F6@
1 FAMS @F12@
```

Well, yeah.  That's GEDCOM.  The leading number on each row?  Indention level.  This is a serialization of a tree structure with references (the `@F11@`` stuff).  Whenever anyone has to read a non-trival amount of this stuff, they just do a substitution on the indention numbers to actually indent it.  What we should probably do is translate it YAML and expand the tags.  Here's what that would look like (with some minor alterations to improve comprehensibility):

```yaml
individual: &I25
    name: Thomas Trask /Wetmore/ Sr
    sex:  M
    events:
        birth:
            date:     13 March 1866
            place:    St. Mary's Bay, Digby, Nova Scotia
            source:   Social Security application
        naturalization:
            name:     Thomas T. Wetmore
            date:     26 October 1888
            place:    Norwich, New London, Connecticut
            age:      22 years
            court:    New London County Court of Common Pleas
            source:   court record from National Archives
        occupation: Antiques Dealer
        death:
            name:     Thomas Trask Wetmore
            date:     17 February 1947
            place:    New London, New London, Connecticut
            age:      80 years, 11 months, 4 days
            cause:    Heart Attack
            source:   New London Death Records
    families:
        child-of: *F11
        spouse-of: *F6
        spouse-of: *F12
```

It looks like Florian Gross [has written a script to do this](https://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-talk/119415), in Ruby.
