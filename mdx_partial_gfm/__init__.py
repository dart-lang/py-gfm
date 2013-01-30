# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from markdown.extensions import Extension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.smart_strong import SmartEmphasisExtension
from markdown.extensions.tables import TableExtension

import gfm

def makeExtension(configs=None):
    return PartialGithubFlavoredMarkdownExtension(configs=configs)

class PartialGithubFlavoredMarkdownExtension(Extension):
    """An extension that's as compatible as possible with GFM.

    This extension aims to be compatible with the variant of GFM that GitHub
    uses for Markdown-formatted gists and files (including READMEs). This
    variant seems to have all the extensions described in the `GFM
    documentation`_, except:

    - Newlines in paragraphs are not transformed into ``br`` tags.
    - Intra-Github links to commits, repositories, and issues are not supported.

    .. _the GFM documentation: http://github.github.com/github-flavored-markdown
    """

    def extendMarkdown(self, md, md_globals):
        # Built-in extensions
        FencedCodeExtension().extendMarkdown(md, md_globals)
        SmartEmphasisExtension().extendMarkdown(md, md_globals)
        TableExtension().extendMarkdown(md, md_globals)

        # Custom extensions
        gfm.AutolinkExtension().extendMarkdown(md, md_globals)
        gfm.AutomailExtension().extendMarkdown(md, md_globals)
        gfm.HiddenHiliteExtension([
            ('guess_lang', 'False'),
            ('css_class', 'highlight')
        ]).extendMarkdown(md, md_globals)
        gfm.SemiSaneListExtension().extendMarkdown(md, md_globals)
        gfm.SpacedLinkExtension().extendMarkdown(md, md_globals)
        gfm.StrikethroughExtension().extendMarkdown(md, md_globals)
