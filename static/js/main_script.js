//main화면에 대한 js

        // 년월 리스트
        var yearMonths = [
            "2015-01", "2015-02", "2015-03", "2015-04", "2015-05", "2015-06",
            "2015-07", "2015-08", "2015-09", "2015-10", "2015-11", "2015-12",
            "2016-01", "2016-02", "2016-03", "2016-04", "2016-05", "2016-06",
            "2016-07", "2016-08", "2016-09", "2016-10", "2016-11", "2016-12",
            "2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06",
            "2017-07", "2017-08", "2017-09", "2017-10", "2017-11", "2017-12",
            "2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06",
            "2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12",
            "2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06",
            "2019-07", "2019-08", "2019-09", "2019-10", "2019-11", "2019-12",
            "2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06",
            "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12",
            "2021-01", "2021-02", "2021-03", "2021-04", "2021-05", "2021-06",
            "2021-07", "2021-08", "2021-09", "2021-10", "2021-11", "2021-12",
            "2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06",
            "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12",
            "2023-01", "2023-02", "2023-03", "2023-04", "2023-05", "2023-06",
            "2023-07", "2023-08", "2023-09"
        ]

        var slider = document.getElementById("myRange");
        var output = document.getElementById("value");
        // 초기화
        output.innerHTML = yearMonths[slider.value];

        // 슬라이더 값 변경 시 이벤트 처리
        slider.oninput = async function () {
            currentyear = yearMonths[this.value];
            output.innerHTML = currentyear

            // 데이터 다시 불러오기
            await addMarkersForCountries();

            // 차트 다시 그리기
            await DrawChart(currentyear, eng_name_param, countriesScore);
        };

        // 현재 년월
        var currentyear = yearMonths[0];

        var chartTypeIndex = 0; // 현재 차트 인덱스

        var eng_name_param; // 영어 이름을 저장할 변수

        var countriesScore; // 전역에서 선언
        
        // chart 타입
        var chartTypes = [
            'line',          // 선 그래프
            'bar',           // 막대 그래프
            'radar',         // 레이더 차트
            'polarArea',     // 극지 차트
            // 'doughnut',      // 도넛 차트
            // 'bubble',        // 버블 차트
            // 'scatter',       // 산점도 차트
            // 'pie',           // 파이 차트
        ];

        // 여러 개의 사용자 정의 아이콘 정의
        const customIcons = {
            icon1: L.icon({
                iconUrl: '/static/images/total20.png',
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -32]
            }),
            icon2: L.icon({
                iconUrl: '/static/images/total40.png',
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -32]
            }),
            icon3: L.icon({
                iconUrl: '/static/images/total60.png',
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -32]
            }),
            icon4: L.icon({
                iconUrl: '/static/images/total80.png',
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -32]
            }),
            icon5: L.icon({
                iconUrl: '/static/images/total20.png',
                iconSize: [32, 32],
                iconAnchor: [16, 32],
                popupAnchor: [0, -32]
            }),
        };

        // 년, 월 스코어를 가지고 옴
        function get_countries_score_year_and_month() {
            return fetch('/get_countries_score_year_and_month')
                .then(get_score => get_score.json())
                .catch(error => console.error('국가 데이터를 가져오는 중 오류 발생:', error));
        }

        // map 객체
        var map = L.map('map').setView([26.73942742009539, 29.932013370889234], 3);
        
        //이거 추가 안하면 맵 못씀
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // 차트 참조 변수
        var chartInstance;

        var container = document.getElementById('chart');
        var sidebar = document.getElementById('sidebar');

        map.on('zoomend', function() {
            var currentZoom = map.getZoom();

            console.log('Current Zoom Level: ', currentZoom);

            if (currentZoom < 3) {
                map.setZoom(3);
            }
        });

        
        async function DrawChart(currentyear, eng_name, countriesScore) {
            var data = {
                labels: ['경제', '안전', '교통', '가격', '음식'],
                datasets: [{
                    label: '점수',
                    data: [
                        countriesScore[currentyear][eng_name]['economy'],
                        countriesScore[currentyear][eng_name]['safety'],
                        countriesScore[currentyear][eng_name]['transportation'],
                        countriesScore[currentyear][eng_name]['price'],
                        countriesScore[currentyear][eng_name]['food'],
                    ],
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2
                }]
            };
        
            var ctx = document.getElementById('Chartcnv').getContext('2d');
        
            // 이전 차트가 존재하면 파괴
            if (chartInstance) {
                await chartInstance.destroy();
            }
        
            // 차트 생성자
            chartInstance = new Chart(ctx, {
                type: chartTypes[chartTypeIndex], // 수정된 부분
                data: data,
                options: {
                    maintainAspectRatio: false,
                    responsive: false,
                    width: 300,
                    height: 300,
                    scales: {
                        r: {
                            beginAtZero: true,
                            max: 100
                        }
                    }
                }
            });
        }

        // 위도, 경도, kr이름, eng이름 데이터 가져옴
        function getCountriesData() {
            return fetch('/get_countries_data')
                .then(response => response.json())
                .catch(error => console.error('Error fetching countries data:', error));
        }

        var markers = []; // 전역으로 이동

        function addMarkersForCountries() {
            Promise.all([getCountriesData(), get_countries_score_year_and_month()])
                .then(([countriesData, scores]) => {
                    countriesScore = scores; // 전역 변수에 할당
                    markers.forEach(marker => marker.remove()); // 이전 마커 제거
                    markers = []; // 마커 초기화

                    countriesData.forEach(country => {
                        // 국가의 위도와 경도 속성이 있다고 가정합니다.
                        const lat = country.lat;
                        const lng = country.lng;
                        
                        const name = country.name;
                        const engname = country.eng_name;

                        // 국가에 따라 아이콘 선택
                        let icon;

                        if(countriesScore[currentyear][engname]['total'] == 100){
                            icon = customIcons.icon5;
                        }
                        else if (countriesScore[currentyear][engname]['total'] >= 80) {
                            icon = customIcons.icon4;
                        } else if (countriesScore[currentyear][engname]['total'] >= 60) {
                            icon = customIcons.icon3;
                        } else if (countriesScore[currentyear][engname]['total'] >= 40) {
                            icon = customIcons.icon2;
                        } else {
                            icon = customIcons.icon1;
                        }

                        // Leaflet 마커 생성
                        const marker = L.marker([lat, lng], { icon: icon }).addTo(map);

                        // 오류 코드
                        const popupContent =
                                            `<strong style="text-align: center;">여행 지수: ${countriesScore[currentyear][engname]['total']}</strong>`;

                        marker.bindPopup(popupContent);
                        
                        markers.push(marker); // 생성된 마커를 markers 배열에 추가

                        // 클릭 이벤트 추가
                        marker.on('click', function (event) {
                            showSidebar(event, country.name, country.eng_name, countriesScore, marker);
                        });
                    });
                })
                .then(() => {
                    // 이제 markers 배열에 모든 마커가 들어있습니다.
                    console.log(markers);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
            }

        document.addEventListener('DOMContentLoaded', addMarkersForCountries);

        // showSidebar 함수를 비동기 함수로 변경
        async function showSidebar(event, kr_name, eng_name, countriesScore, marker) {
            document.addEventListener('click', closeSidebarOutside);

            // eng_name 업데이트
            eng_name_param = eng_name;

            // 해당하는 국가의 그래프
            await DrawChart(currentyear, eng_name, countriesScore);

            // 나머지 국가 정보를 사이드바에 추가
            await updateSidebar(kr_name);

            // map 동작 제어
            map.dragging.disable();
            map.touchZoom.disable();
            map.doubleClickZoom.disable();
            map.scrollWheelZoom.disable();

            // 사이드바를 나타나게 설정
            sidebar.style.right = '0';
            sidebar.style.display = 'inline';
        }

        // updateSidebar 함수를 비동기 함수로 변경
        async function updateSidebar(country_name) {
            var countryNameElement = document.getElementById('countryName');
            var flagElement = document.getElementById('flag');
            var nationInfoElement = document.getElementById('nationinfo');

            try {
                // AJAX를 이용하여 Flask 엔드포인트에 요청
                const response = await fetch('/get_country_data/' + country_name);
                const countryData = await response.json();
                countryNameElement.innerText = country_name;  // 국가 이름 업데이트
                // 여기에 국기 사진, 정보 업데이트 등 다른 업데이트 코드 추가
                flagElement.innerHTML = '<img src="' + countryData.image_url + '" alt="Flag">';
                nationInfoElement.innerHTML = '<p>' + countryData.info + '</p>';
            } catch (error) {
                console.error('Error fetching country data:', error);
            }
        }
        
        
        function closeSidebarOutside(event) {
            // event.target이 노드인지 확인
            if (!(event.target instanceof Node)) {
                return;
            }
        
            // 만약 버튼이나 슬라이더를 클릭한 경우 함수를 종료하고 리턴
            if (
                event.target.id === 'nextbtn' ||
                event.target.id === 'beforebtn' ||
                event.target.id === 'myRange' // 슬라이더 클릭인 경우 추가
            ) {
                return;
            }
        
            // markers 배열에 대한 순회
            for (let i = 0; i < markers.length; i++) {
                // 각 마커에 대해 클릭된 지점이 포함되어 있는지 확인
                if (markers[i]._icon && markers[i]._icon.contains && markers[i]._icon.contains(event.target)) {
                    // 클릭된 지점이 마커에 속한 경우 함수를 종료하고 리턴
                    return;
                }
            }
        
            // 클릭된 지점이 어떠한 마커에도 속하지 않으면 사이드바를 닫습니다.
            closeSidebar();
        }

        function closeSidebar() {
            // 맵 상호작용 초기화
            map.dragging.enable();
            map.touchZoom.enable();
            map.doubleClickZoom.enable();
            map.scrollWheelZoom.enable();
        
            // 사이드바 숨기기
            sidebar.style.right = '-30vw';
            
            // 차트 인덱스 초기화
            chartTypeIndex = 0;
        
            // 사이드바 외부를 클릭하여 닫는 이벤트 리스너 제거
            document.removeEventListener('click', closeSidebarOutside);
        }

        // 다음 버튼 클릭 시 발생하는 함수
        document.getElementById('nextbtn').addEventListener('click', function () {
            if (chartTypeIndex < chartTypes.length - 1) {
                chartTypeIndex++;
                DrawChart(currentyear, eng_name_param, countriesScore);
            }
        });

        // 이전 버튼 클릭 시 발생하는 함수
        document.getElementById('beforebtn').addEventListener('click', function () {
            if (chartTypeIndex > 0) {
                chartTypeIndex--;
                DrawChart(currentyear, eng_name_param, countriesScore);
            }
        });

