import flet as ft

class Player:
    def __init__(self, url):
        self.state = "stopped"
        self.audio = ft.Audio(src=url, volume=0.3,
                              on_loaded=lambda _:print('on_loaded'),
                              on_position_changed=lambda e:print(f'on_position_changed: {e.data}'),
                              on_state_changed=lambda e:print(f'on_state_change: {e.data}'))

    def toggle_play(self):
        print(self.audio)
        if self.state == "stopped":
            self.audio.play()
            self.state = "playing"
        elif self.state == "paused":
            self.audio.resume()
            self.state = "playing"
        else:
            self.audio.pause()
            self.state = "paused"

def main(page : ft.Page):

    def on_undo(e):
        page.controls.pop()
        page.update()

    def on_click(e):
        page.add(ft.Text("Hello again"))
        page.snack_bar = ft.SnackBar(content=ft.Text("OK"), action="undo", on_action=on_undo)
        page.snack_bar.open = True
        page.update()

    page.title = "Testing"
    player = Player('https://luan.xyz/files/audio/ambient_c_motion.mp3')
    page.overlay.append(player.audio)
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.add(ft.Row([ft.Text("Hello world!", size=40), ft.IconButton(icon=ft.icons.PLAY_CIRCLE, icon_size=50,
                                                            on_click=lambda _:player.toggle_play())],
                    alignment=ft.MainAxisAlignment.CENTER))
    page.update()

if __name__ == "__main__":
    ft.app(target=main)