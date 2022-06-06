from ejercicio_musical import MediaPlayerQueue, Track, QueueNode

track1 = Track("Highway to hell")
track2 = Track("GO!")
track3 = Track("Light years")
track4 = Track("Heartbreaker")
track5 = Track("Breath me")
track6 = Track("How to dissapear completely")

media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.add_track(track6)

print(media_player.play())