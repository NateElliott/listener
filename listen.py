from audio_in import amplitude

tt = amplitude.Average()


# TV 0.007


tt.tap_threshold = 0.0035


quite_wait = 0
buffer = 0


while True:
    current_buffer = tt.listen()
    buffer += 1
    if buffer == 100: # 5 seconds
        print quite_wait
        buffer = 0

        break


    if not current_buffer:
        quite_wait += 1
    else:
        print buffer,"*" * int(current_buffer * 250)


