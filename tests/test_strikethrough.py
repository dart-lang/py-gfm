# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestStrikethrough(TestCase):
    def setUp(self):
        self.strikethrough = gfm.StrikethroughExtension([])

    def test_double_tilde_strikes(self):
        self.assert_renders("""
        <p>This is <del>struck</del>, and so <del>is this</del>.</p>
        """, """
        This is ~~struck~~, and so ~~is this~~.
        """, [self.strikethrough])

    def test_single_tilde_doesnt_strike(self):
        self.assert_renders("""
        <p>This is ~not struck~, and this tilde <del>doesn't~stop~it</del>.</p>
        """, """
        This is ~not struck~, and this tilde ~~doesn't~stop~it~~.
        """, [self.strikethrough])

    def test_strikethrough_nests(self):
        self.assert_renders("""
        <p><del><strong>outer</strong></del>, <strong><del>inner</del></strong>.</p>
        """, """
        ~~**outer**~~, **~~inner~~**.
        """, [self.strikethrough])

    def test_extra_tildes_dont_cause_strikethrough(self):
        self.assert_renders("""
        <p>~~~foo~~~, ~~~bar~~, ~~~~baz~~~~</p>
        """, """
        ~~~foo~~~, ~~~bar~~, ~~~~baz~~~~
        """, [])
