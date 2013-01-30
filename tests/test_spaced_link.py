# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestMultilineLink(TestCase):
    def setUp(self):
        self.spaced_link = gfm.SpacedLinkExtension([])

    def test_normal_link(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link](href)
        """, [self.spaced_link])

    def test_normal_reference(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link][id]

        [id]: href
        """, [self.spaced_link])

    def test_normal_image_link(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt](href)
        """, [self.spaced_link])

    def test_normal_image_reference(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt][id]

        [id]: href
        """, [self.spaced_link])

    def test_spaced_link(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link]  (href)
        """, [self.spaced_link])

    def test_spaced_reference(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link]  [id]

        [id]: href
        """, [self.spaced_link])

    def test_spaced_image_link(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt]  (href)
        """, [self.spaced_link])

    def test_spaced_image_reference(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt]  [id]

        [id]: href
        """, [self.spaced_link])

    def test_multiline_link(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link]
        (href)
        """, [self.spaced_link])

    def test_multiline_reference(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link]
        [id]

        [id]: href
        """, [self.spaced_link])

    def test_multiline_image_link(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt]
        (href)
        """, [self.spaced_link])

    def test_multiline_image_reference(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt]
        [id]

        [id]: href
        """, [self.spaced_link])

    def test_multiline_and_spaced_link(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link] 
          (href)
        """, [self.spaced_link])

    def test_multiline_and_spaced_reference(self):
        self.assert_renders("""
        <p><a href="href">link</a></p>
        """, """
        [link] 
          [id]

        [id]: href
        """, [self.spaced_link])

    def test_multiline_and_spaced_image_link(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt] 
          (href)
        """, [self.spaced_link])

    def test_multiline_and_spaced_image_reference(self):
        self.assert_renders("""
        <p><img alt="alt" src="href" /></p>
        """, """
        ![alt] 
          [id]

        [id]: href
        """, [self.spaced_link])
