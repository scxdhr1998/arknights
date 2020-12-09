package com.arkights;

import okhttp3.*;



public class ac {
    public static void main(String[] args) throws Exception{
        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        Request request = new Request.Builder()
                .url("https://ak.hypergryph.com/user/api/inquiry/gacha?page=1")
                .method("GET", null)
                .addHeader("Cookie", "acw_tc=77a7dc1c16074307995866247e8a9a09be9b738bd7c478071478eb6198; _uab_collina=160743077639007371272871; csrf_token=h749ltfPNbDNkfGxjEudDeN5; _ga=GA1.2.1991390729.1607430778; _gid=GA1.2.705102461.1607430778; HG_ACCOUNT=6dsBljPsKbKNkyA0dAe89WJH4mP0R4chddBTp960ka1yHUJcg8G-DO3D3aTF-hJk2OuQkfQKVsv2WaCkyKva0k2SRxybF3kudCHGwS5s-yzcp7NGtuCvfwiFLmkzG8NDTsMUQe0l1z9pwkatXcC9Hhb-QegnzuwYQdIDqqSUegQwD3wtxGbOQd9gJrMYvmFM923UEtv79hULsAj4Uju-oKEoXG5Qpc7KTgW7V8zNimrRyPcjsK32p7vG5eM_li4uDEM9QEMCawE4e-smSlxE-sgtK4igZeAJhf-JlGpAkCU=; _gat=1; u_asec=099%23KAFEBEEKEcdEhYTLEEEEEpEQz0yFZ6VTDXyFA603DcBoW6VHDu9MQ6VwlYFETJDovlvUE7TxEnJMEF2ZMJK4IqCcXyTDfJ6%2F1HN7sHGtIiERvwyY6LMQRKnyMOFYqwP%2Bk6Arti7WoZ7fBB8sIhj2qNf3yUQGBHz4DYDk%2B1A4kLHBinubokjr0dMTEHB5lGEiaquYSpXfNVopL3exOfZCcMPcOfZd4OhnwBZgSOJwNsj6weJIzPuLbIOqPfZYDw%2BV7Jns8Ouj6Rac1WyTzPdQ6wZprtysLO8CivZtSWB7Pw47sEFEp3llsyaSt3lllllzn3iS1pRlluUdt37qn3llWLaStEGdllle33iSwwAoE7EIlllbCOyOakarE7EhT3l%2F%2FoasjYFET%2FdEsyaStHQTEEi5DEEEDEFET3llsR4%3D")
                .build();
        Response response = client.newCall(request).execute();
        String responseData = response.body().string();
        System.out.println(responseData);
    }


}
