$(function () {

    // We use an inline data source in the example, usually data would
    // be fetched from a server
    var activeChannels = [0, 0, 0, 0, 0, 0, 0, 0];
    var data = [],
        totalPoints = 300;

    function getRandomData() {

        if (data.length > 0)
            data = data.slice(1);

        // Do a random walk

        while (data.length < totalPoints) {


            var prev = data.length > 0 ? data[data.length - 1] : 50,
                y = prev + Math.random() * 10 - 5;

            if (y < 0) {
                y = 0;
            } else if (y > 100) {
                y = 100;
            }

            data.push(y);
        }

        // Zip the generated y values with the x values

        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }

        return res;
    }

    function getWLMdata() {

        if (data.length > 0)
            data = data.slice(1);

        // Do a random walk

        while (data.length < totalPoints) {


            y = 2;

            if (y < 0) {
                y = 0;
            } else if (y > 100) {
                y = 100;
            }

            data.push(y);
        }

        // Zip the generated y values with the x values

        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }

        return res;
    }

    function getDataChannel(chan) {
        return chan
    }


    // Set up the control widget

    var updateInterval = 100;
    $("#updateInterval").val(updateInterval).change(function () {
        var v = $(this).val();
        if (v && !isNaN(+v)) {
            updateInterval = +v;
            if (updateInterval < 1) {
                updateInterval = 1;
            } else if (updateInterval > 2000) {
                updateInterval = 2000;
            }
            $(this).val("" + updateInterval);
        }
    });

    {#            var plot = $.plot("#graph", [getWLMdata()], {#
    }
        {#            var plot = $.plot("#graph", [getWLMdata()], {#
        }
            {#                series: {#
            }
                {#                    shadowSize: 0	// Drawing is faster without shadows#}
                    {#
                    }
                ,#
                }
                {#                yaxis: {#
                }
                    {#                    min: 0,#
                    }
                    {#                    max: 10#
                    }
                    {#
                    }
                ,#
                }
                {#                xaxis: {#
                }
                    {#                    show: true#
                    }
                    {#
                    }#
                }
                {#
                }
            )
            ;#
        }


        function update() {


            {#                plot.setData([getWLMdata(), getWLMdata()]);#
            }

            // Since the axes don't change, we don't need to call plot.setupGrid()

            {#                plot.draw();#
            }
            setTimeout(update, updateInterval);


            if (activeChannels[0]) {
                $("#chan1").text("Master: " + wlmData[1] + " THz");

                {#                    $("#chan1").text("Master: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
                }
            } else {
                $("#chan1").text("Master: OFF")
            }
            if (activeChannels[1]) {
                $("#chan2").text("MOT COOLING: " + wlmData[2] + " THz")
            } else {
                $("#chan2").text("MOT COOLING: OFF")
            }
            if (activeChannels[2]) {
                $("#chan3").text("Chan3: " + wlmData[3] + " THz")
            } else {
                $("#chan3").text("Chan3: OFF")
            }
            if (activeChannels[3]) {
                $("#chan4").text("Chan4: " + wlmData[4] + " THz")
            } else {
                $("#chan4").text("Chan4: OFF")
            }
            if (activeChannels[4]) {
                $("#chan5").text("Chan5: " + wlmData[5] + " THz")
            } else {
                $("#chan5").text("Chan5: OFF")
            }
            if (activeChannels[5]) {
                $("#chan6").text("Chan6: " + wlmData[6] + " THz")
            } else {
                $("#chan6").text("Chan6: OFF")
            }
            if (activeChannels[6]) {
                $("#chan7").text("Chan7: " + wlmData[7] + " THz")
            } else {
                $("#chan7").text("Chan7: OFF")
            }
            if (activeChannels[7]) {
                $("#chan8").text("Chan8: " + wlmData[8] + " THz")
            } else {
                $("#chan8").text("Chan8: OFF")
            }


            {#                $("#chan2").text("MOT COOLING: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan3").text("MOT REPUMP: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan4").text("Chan 4: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan5").text("Chan 5: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan6").text("Chan 6: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan7").text("Chan 7: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }
            {#                $("#chan8").text("Chan 8: " + (Math.random() + 384.230406373).toFixed(5) + " THz")#
            }

        }

        update();

        $('#chan1Toggle').change(function () {
            if ($(this).prop('checked')) {
                activeChannels[0] = 1;
            } else {
                activeChannels[0] = 0;
            }


            {#                JSON.stringify(activeChannels);#
            }
            $.ajax({
                method: 'POST',
                contentType: "application/json",
                url: '_setWLMChannels',
                data: JSON.stringify({'activeChannels': activeChannels}),
                error: function (e) {
                    console.log(e)
                },
                dataType: 'json'
            });
        });

        {#                $.post({
            {
                url_for('setWLMChannels'), activeChannels
            :
                "Gal"
            }
        }
        }
    )#
    }


    $('#chan2Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[1] = 1;
        } else {
            activeChannels[1] = 0;
        }


    });
    $('#chan3Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[2] = 1;
        } else {
            activeChannels[2] = 0;
        }


    });
    $('#chan4Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[3] = 1;
        } else {
            activeChannels[3] = 0;
        }


    });
    $('#chan5Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[4] = 1;
        } else {
            activeChannels[4] = 0;
        }


    });
    $('#chan6Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[5] = 1;
        } else {
            activeChannels[5] = 0;
        }


    });
    $('#chan7Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[6] = 1;
        } else {
            activeChannels[6] = 0;
        }


    });
    $('#chan8Toggle').change(function () {
        if ($(this).prop('checked')) {
            activeChannels[7] = 1;
        } else {
            activeChannels[7] = 0;
        }


    });


    var wlmData = {};
    (function worker() {
        $.ajax({
            dataType: "json",
            url: '_getWLMData/',
            success: function (data) {
                wlmData = data;

            },
            complete: function () {
                // Schedule the next request when the current one's complete
                setTimeout(worker, 100);
            }
        });
    })();

});
$(".ChanToggleButton").click(function () {
    $(this).button('toggle');
});
