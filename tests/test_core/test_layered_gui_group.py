import pytest
import pygame

from pygame_gui.core.layered_gui_group import GUISprite, LayeredGUIGroup


class MyProperSprite(GUISprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.blendmode = 0
        self.visible = 1

    def update(self, time_delta: float):
        pass


class MyDodgySprite1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

    def update(self, time_delta: float):
        pass


class MyDodgySprite2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.visible = 1

    def update(self, time_delta: float):
        pass


class MyDodgySprite3(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.blendmode = 0
        self.visible = 1


class TestUIElement:
    def test_remove_sprite_from_group(self, _init_pygame, default_ui_manager):

        group = LayeredGUIGroup()

        proper_sprite = MyProperSprite(group)

        proper_sprite.remove(group)

        assert len(group.sprites()) == 0

    def test_add_dodgy_sprites(self, _init_pygame, default_ui_manager):
        group = LayeredGUIGroup()

        with pytest.raises(AttributeError):
            MyDodgySprite1(group)

        with pytest.raises(AttributeError):
            MyDodgySprite2(group)

        with pytest.raises(AttributeError):
            MyDodgySprite3(group)

    def test_sprite_set_layer_before_add(self, _init_pygame, default_ui_manager):
        group = LayeredGUIGroup()

        sprite1 = MyProperSprite()
        sprite1.layer = 2

        sprite2 = MyProperSprite()
        sprite2.layer = 0

        sprite3 = MyProperSprite()
        sprite3.layer = 1

        sprite1.add(group)
        sprite2.add(group)
        sprite3.add(group)

        assert len(group.layers()) == 3 and group.layers() == [0, 1, 2]

    def test_print_sprite(self, _init_pygame, default_ui_manager):
        group = LayeredGUIGroup()

        sprite1 = MyProperSprite()

        print(sprite1)


if __name__ == '__main__':
    pytest.console_main()