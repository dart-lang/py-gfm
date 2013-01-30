# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from test_case import TestCase

class TestGfm(TestCase):
    def test_fenced_code(self):
        self.assert_renders("""
        <div class="highlight"><pre>foo
        </pre></div>
        """, """
        ```
        foo
        ```
        """, ['gfm'])

    def test_nl2br(self):
        self.assert_renders("""
        <p>foo<br />
        bar</p>
        """, """
        foo
        bar
        """, ['gfm'])

    def test_smart_emphasis(self):
        self.assert_renders("""
        <p>foo__bar__baz</p>
        """, """
        foo__bar__baz
        """, ['gfm'])

    def test_table(self):
        self.assert_renders("""
        <table>
        <thead>
        <tr>
        <th>First Header</th>
        <th>Second Header</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        </tbody>
        </table>
        """, """
        First Header  | Second Header
        ------------- | -------------
        Content Cell  | Content Cell
        Content Cell  | Content Cell
        """, ['gfm'])

    def test_hilite(self):
        self.assert_renders("""
        <div class="highlight"><pre><span class="k">def</span>
        </pre></div>
        """, """
        ```.python
        def
        ```
        """, ['gfm'])

    def test_semi_sane_lists(self):
        self.assert_renders("""
        <ul>
        <li>foo</li>
        </ul>
        <ol>
        <li>bar</li>
        </ol>
        """, """
        * foo

        1. bar
        """, ['gfm'])

    def test_autolink(self):
        self.assert_renders("""
        <p><a href="http://foo.com/bar">http://foo.com/bar</a></p>
        """, """
        http://foo.com/bar
        """, ['gfm'])

    def test_automail(self):
        self.assert_renders("""
        <p><a href="mailto:foo@bar.com">foo@bar.com</a></p>
        """, """
        foo@bar.com
        """, ['gfm'])

    def test_strikethrough(self):
        self.assert_renders("""
        <p>This is <del>struck</del>.</p>
        """, """
        This is ~~struck~~.
        """, ['gfm'])

    def test_spaced_link(self):
        self.assert_renders("""
        <p><a href="href">text</a></p>
        """, """
        [text] (href)
        """, ['gfm'])
