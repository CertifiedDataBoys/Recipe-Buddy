var timerObj = {
    timerBeingSet: true,
    timerRunning: false,
    timerInterval: null,
    timerEndedInterval: null,
    timerTimestamp: null,
    timerEnded: false,
    pausedSeconds: null,
    secondsLeft: null
}

$(document).ready(function() {
    const html = `
        <div id="timer-body" class="timer-body text-center">
            <h4 class="text-center">Timer ⏱️</h4>
            <h6 id="timer-time" class="text-center timer-hidden">00:00</h6>
            <div id="timer-input-group" class="timer-input-group input-group">
                <input type="number" id="timer-minutes" class="timer-input text-center form-control form-control-sm" placeholder="mm" min="0" max="59">
                <span class="input-group-addon">&nbsp;:&nbsp;</span>
                <input type="number" id="timer-seconds" class="timer-input text-center form-control form-control-sm" placeholder="ss" min="0" max="59">
            </div>
            <input class="play-sound-chk form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
            <label class="play-sound-chk form-check-label" for="flexCheckChecked">
                Play sound?
            </label><br class="play-sound-chk">
            <a href="#" id="start-timer" class="btn timer-primary-btn timer-hidden">Start</a>
            <a href="#" id="set-timer" class="btn timer-primary-btn">Set Timer</a>
            <audio controls loop="true" preload="auto" id="timer-audio" class="timer-hidden">
                <source src="/timer.mp3" type="audio/mpeg">
            </audio>
        </div>
    `;
    $("#main").append(html);

    if (SessionStorageHelper.get('timer-play-sound') !== {} && SessionStorageHelper.get('timer-play-sound') !== null) {
        $("#flexCheckChecked").prop('checked', SessionStorageHelper.get('timer-play-sound').val);
    } else {
        $("#flexCheckChecked").prop('checked', true);
    }

    if (SessionStorageHelper.get('timer') !== {} && SessionStorageHelper.get('timer') !== null) {
        detectTimerObj(SessionStorageHelper.get('timer'));
    }

    $("#start-timer").click(function() {
        if (timerObj.timerEnded && !timerObj.timerRunning) {
            $("#start-timer").text("Start");
            $("#set-timer").removeClass("timer-hidden");
            endTimerEndedAnimation();
            timerObj.timerBeingSet = false;
        } else {
            if (timerObj.timerRunning) {
                $("#set-timer").removeClass("timer-hidden");
                var now = Math.round(new Date().getTime() / 1000);
                timerObj.pausedSeconds = timerObj.timerTimestamp - now;
                stopTimer();
            } else {
                if (timerObj.pausedSeconds !== null) {
                    timerObj.secondsLeft = timerObj.pausedSeconds;
                }
                startTimer(timerObj.secondsLeft);
            }
        }
    });

    $("#set-timer").click(function() {
        if (!timerObj.timerBeingSet) {
            $("#timer-input-group").removeClass("timer-hidden");
            $(".play-sound-chk").removeClass("timer-hidden");
            $("#timer-time").addClass("timer-hidden");
            $("#set-timer").removeClass("timer-set-btn");
            $("#set-timer").addClass("timer-primary-btn");
            $("#start-timer").addClass("timer-hidden");
            timerObj = {
                timerBeingSet: false,
                timerRunning: false,
                timerInterval: null,
                timerEndedInterval: null,
                timerTimestamp: null,
                timerEnded: false,
                pausedSeconds: null,
                secondsLeft: null
            }
            SessionStorageHelper.clear();
        } else {
            var minutes = $("#timer-minutes").val();
            if (minutes == "")
                minutes = 0;
            var seconds = $("#timer-seconds").val();
            if (seconds == "")
                seconds = 0;
            var time = (parseInt(minutes) * 60) + parseInt(seconds);
            if (time == 0) {
                alert("Please set a time greater than 0");
                return;
            }
            if (minutes > 59 || minutes < 0) {
                alert("Please set minutes between 0 and 59");
                return;
            }
            if (seconds > 59 || seconds < 0) {
                alert("Please set seconds between 0 and 59");
                return;
            }

            timerObj.secondsLeft = time;

            $("#timer-time").html(padTime(minutes) + ":" + padTime(seconds));
            $("#timer-input-group").addClass("timer-hidden");
            $(".play-sound-chk").addClass("timer-hidden");
            $("#timer-time").removeClass("timer-hidden");
            $("#set-timer").removeClass("timer-primary-btn");
            $("#set-timer").addClass("timer-set-btn");
            $("#start-timer").removeClass("timer-hidden");
            $("#set-timer").removeClass("timer-hidden");
        }
        timerObj.timerBeingSet = !timerObj.timerBeingSet;
    });

    $(".timer-input").change(function() {
        if ($(this).val() > 59) {
            $(this).val(59);
            return;
        }
        if ($(this).val().length == 1) {
            $(this).val('0' + $(this).val());
            return;
        }
    });

    $("#flexCheckChecked").change(function() {
        SessionStorageHelper.save('timer-play-sound', { val: $(this).prop('checked') });
    });
});

function detectTimerObj(obj) {
    const now = Math.round(new Date().getTime() / 1000);
    if (obj.timerTimestamp - now < 0) {
        // If timer ended animation is still running
        $("#timer-time").html("00:00");
        $("#timer-input-group").addClass("timer-hidden");
        $(".play-sound-chk").addClass("timer-hidden");
        $("#timer-time").removeClass("timer-hidden");
        $("#set-timer").removeClass("timer-primary-btn");
        $("#set-timer").addClass("timer-set-btn");
        $("#start-timer").removeClass("timer-hidden");
        $("#set-timer").addClass("timer-hidden");
        $("#start-timer").text("Pause");
        startTimerEndedAnimation();
        timerObj.timerEnded = true;
        timerObj.timerRunning = false;
        timerObj.timerBeingSet = false;
    } else if (obj.timerRunning) {
        // If timer is running
        const now = Math.round(new Date().getTime() / 1000);
        const distance = obj.timerTimestamp - now;
        timerObj.timerTimestamp = obj.timerTimestamp;
        timerObj.secondsLeft = distance;
        $("#timer-time").text(padTime(Math.floor(distance / 60)) + ":" + padTime(Math.floor(distance % 60)));
        startTimer(distance);
        timerObj.timerBeingSet = false;
        $("#timer-input-group").addClass("timer-hidden");
        $(".play-sound-chk").addClass("timer-hidden");
        $("#timer-time").removeClass("timer-hidden");
        $("#set-timer").removeClass("timer-primary-btn");
        $("#set-timer").addClass("timer-set-btn");
        $("#start-timer").removeClass("timer-hidden");
        $("#set-timer").addClass("timer-hidden");
    } else if (!obj.timerRunning && obj.pausedSeconds !== null) {
        // If timer is paused
        timerObj.secondsLeft = obj.pausedSeconds;
        timerObj.timerBeingSet = false;
        timerObj.timerEnded = false;
        timerObj.timerRunning = false;
        $("#timer-time").text(padTime(Math.floor(obj.pausedSeconds / 60)) + ":" + padTime(Math.floor(obj.pausedSeconds % 60)));
        $("#timer-input-group").addClass("timer-hidden");
        $(".play-sound-chk").addClass("timer-hidden");
        $("#timer-time").removeClass("timer-hidden");
        $("#set-timer").removeClass("timer-primary-btn");
        $("#set-timer").addClass("timer-set-btn");
        $("#start-timer").removeClass("timer-hidden");
    } else {
        // Nothing found, clear timer session
        SessionStorageHelper.clear();
    }
}

function padTime(d) {
    d = parseInt(d);
    if (d < 10)
        return "0" + d;
    return d;
}

function startTimer(inputTime) {
    if ($("#timer-time").text() == "00:00") {
        alert("Please set the timer before attempting to start it again");
        return;
    }
    var time = Math.round(new Date().getTime() / 1000) + inputTime;
    timerObj.timerRunning = true;
    $("#set-timer").addClass("timer-hidden");
    timerObj.timerTimestamp = time;

    var now = Math.round(new Date().getTime() / 1000);
    var distance = time - now;

    var minutes = Math.floor(distance / 60);
    var seconds = Math.floor(distance % 60);

    $("#timer-time").html(padTime(minutes) + ":" + padTime(seconds));

    timerObj.timerInterval = setInterval(function() {
        var now = Math.round(new Date().getTime() / 1000);
        var distance = time - now;

        var minutes = Math.floor(distance / 60);
        var seconds = Math.floor(distance % 60);

        $("#timer-time").html(padTime(minutes) + ":" + padTime(seconds));

        if (distance < 0) {
            clearInterval(timerObj.timerInterval);
            $("#timer-time").html("00:00");
            startTimerEndedAnimation();
            timerObj.timerRunning = false;
            timerObj.timerEnded = true;
            timerObj.secondsLeft = 0;
        }
    }, 1000);
    $("#start-timer").text("Pause");
    SessionStorageHelper.save('timer', timerObj);
}

function stopTimer() {
    clearInterval(timerObj.timerInterval);
    timerObj.timerRunning = false;
    $("#start-timer").text("Start");
    SessionStorageHelper.save('timer', timerObj);
}

function endTimerEndedAnimation() {
    clearInterval(timerObj.timerEndedInterval);
    $("#timer-body").removeClass("timer-anim-bg");
    $("#start-timer").removeClass("timer-anim-btn");
    $("#start-timer").text("Start");
    timerObj.timerEnded = false;
    $("#timer-audio")[0].pause();
    $("#timer-audio")[0].currentTime = 0;
    SessionStorageHelper.clear();
}

function startTimerEndedAnimation() {
    timerObj.timerEndedInterval = setInterval(function() {
        $("#timer-body").toggleClass("timer-anim-bg");
        $("#start-timer").toggleClass("timer-anim-btn");
    }, 1000);
    $("#start-timer").text("Stop");
    if ($("#flexCheckChecked").is(':checked') || (SessionStorageHelper.get('timer-play-sound') !== null && SessionStorageHelper.get('timer-play-sound').val)) {
        $("#timer-audio")[0].play();
        SessionStorageHelper.save('timer', timerObj);
    }
}