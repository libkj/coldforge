# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    coinid = models.IntegerField(blank=True, null=True)
    last_earning = models.IntegerField(blank=True, null=True)
    is_locked = models.IntegerField(blank=True, null=True)
    no_fees = models.IntegerField(blank=True, null=True)
    donation = models.PositiveIntegerField()
    logtraffic = models.IntegerField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=128, db_collation='utf8_bin')
    coinsymbol = models.CharField(max_length=16, blank=True, null=True)
    swap_time = models.PositiveIntegerField(blank=True, null=True)
    login = models.CharField(max_length=45, blank=True, null=True)
    hostaddr = models.CharField(max_length=39, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Algos(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    rent = models.FloatField(blank=True, null=True)
    factor = models.FloatField(blank=True, null=True)
    overflow = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algos'


class Balances(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    onsell = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balances'


class Balanceuser(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    pending = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balanceuser'


class BenchChips(models.Model):
    devicetype = models.CharField(max_length=8, blank=True, null=True)
    vendorid = models.CharField(max_length=12, blank=True, null=True)
    chip = models.CharField(max_length=32, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    maxtdp = models.FloatField(blank=True, null=True)
    blake_rate = models.FloatField(blank=True, null=True)
    blake_power = models.FloatField(blank=True, null=True)
    x11_rate = models.FloatField(blank=True, null=True)
    x11_power = models.FloatField(blank=True, null=True)
    sha_rate = models.FloatField(blank=True, null=True)
    sha_power = models.FloatField(blank=True, null=True)
    scrypt_rate = models.FloatField(blank=True, null=True)
    scrypt_power = models.FloatField(blank=True, null=True)
    dag_rate = models.FloatField(blank=True, null=True)
    dag_power = models.FloatField(blank=True, null=True)
    lyra_rate = models.FloatField(blank=True, null=True)
    lyra_power = models.FloatField(blank=True, null=True)
    neo_rate = models.FloatField(blank=True, null=True)
    neo_power = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    features = models.CharField(max_length=255, blank=True, null=True)
    perfdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bench_chips'


class BenchSuffixes(models.Model):
    vendorid = models.CharField(primary_key=True, max_length=12)
    chip = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'bench_suffixes'


class Benchmarks(models.Model):
    algo = models.CharField(max_length=16)
    type = models.CharField(max_length=8)
    khps = models.FloatField(blank=True, null=True)
    device = models.CharField(max_length=80, blank=True, null=True)
    vendorid = models.CharField(max_length=12, blank=True, null=True)
    chip = models.CharField(max_length=32, blank=True, null=True)
    idchip = models.ForeignKey(BenchChips, models.DO_NOTHING, db_column='idchip', blank=True, null=True)
    arch = models.CharField(max_length=8, blank=True, null=True)
    power = models.PositiveIntegerField(blank=True, null=True)
    plimit = models.PositiveIntegerField(blank=True, null=True)
    freq = models.PositiveIntegerField(blank=True, null=True)
    realfreq = models.PositiveIntegerField(blank=True, null=True)
    memf = models.PositiveIntegerField(blank=True, null=True)
    realmemf = models.PositiveIntegerField(blank=True, null=True)
    client = models.CharField(max_length=48, blank=True, null=True)
    os = models.CharField(max_length=8, blank=True, null=True)
    driver = models.CharField(max_length=32, blank=True, null=True)
    intensity = models.FloatField(blank=True, null=True)
    throughput = models.PositiveIntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'benchmarks'


class Blocks(models.Model):
    coin_id = models.IntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    confirmations = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    workerid = models.IntegerField(blank=True, null=True)
    difficulty_user = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=16, blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)
    blockhash = models.CharField(max_length=128, blank=True, null=True)
    txhash = models.CharField(max_length=128, blank=True, null=True)
    segwit = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'blocks'


class Bookmarks(models.Model):
    idcoin = models.ForeignKey('Coins', models.DO_NOTHING, db_column='idcoin')
    label = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=128)
    lastused = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookmarks'


class Coins(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    symbol = models.CharField(max_length=16, blank=True, null=True)
    symbol2 = models.CharField(max_length=16, blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    market = models.CharField(max_length=64, blank=True, null=True)
    marketid = models.IntegerField(blank=True, null=True)
    master_wallet = models.CharField(max_length=1024, blank=True, null=True)
    charity_address = models.CharField(max_length=1024, blank=True, null=True)
    charity_amount = models.FloatField(blank=True, null=True)
    charity_percent = models.FloatField(blank=True, null=True)
    deposit_address = models.CharField(max_length=1024, blank=True, null=True)
    deposit_minimum = models.FloatField(blank=True, null=True)
    sellonbid = models.IntegerField(blank=True, null=True)
    dontsell = models.IntegerField(blank=True, null=True)
    block_explorer = models.CharField(max_length=1024, blank=True, null=True)
    index_avg = models.FloatField(blank=True, null=True)
    connections = models.IntegerField(blank=True, null=True)
    errors = models.CharField(max_length=1024, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    immature = models.FloatField(blank=True, null=True)
    cleared = models.FloatField(blank=True, null=True)
    available = models.FloatField(blank=True, null=True)
    stake = models.FloatField(blank=True, null=True)
    mint = models.FloatField(blank=True, null=True)
    txfee = models.FloatField(blank=True, null=True)
    payout_min = models.FloatField(blank=True, null=True)
    payout_max = models.FloatField(blank=True, null=True)
    block_time = models.IntegerField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    difficulty_pos = models.FloatField(blank=True, null=True)
    block_height = models.IntegerField(blank=True, null=True)
    target_height = models.IntegerField(blank=True, null=True)
    powend_height = models.IntegerField(blank=True, null=True)
    network_hash = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    reward = models.FloatField(blank=True, null=True)
    reward_mul = models.FloatField(blank=True, null=True)
    mature_blocks = models.IntegerField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    auto_ready = models.IntegerField(blank=True, null=True)
    visible = models.IntegerField(blank=True, null=True)
    no_explorer = models.PositiveIntegerField()
    max_miners = models.IntegerField(blank=True, null=True)
    max_shares = models.IntegerField(blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    conf_folder = models.CharField(max_length=128, blank=True, null=True)
    program = models.CharField(max_length=128, blank=True, null=True)
    rpcuser = models.CharField(max_length=128, blank=True, null=True)
    rpcpasswd = models.CharField(max_length=128, blank=True, null=True)
    serveruser = models.CharField(max_length=45, blank=True, null=True)
    rpchost = models.CharField(max_length=128, blank=True, null=True)
    rpcport = models.IntegerField(blank=True, null=True)
    rpccurl = models.IntegerField()
    rpcssl = models.IntegerField()
    rpccert = models.CharField(max_length=255, blank=True, null=True)
    rpcencoding = models.CharField(max_length=16, blank=True, null=True)
    account = models.CharField(max_length=64)
    hasgetinfo = models.PositiveIntegerField()
    hassubmitblock = models.PositiveIntegerField()
    hasmasternodes = models.IntegerField()
    usememorypool = models.IntegerField(blank=True, null=True)
    usesegwit = models.PositiveIntegerField()
    txmessage = models.IntegerField(blank=True, null=True)
    auxpow = models.IntegerField(blank=True, null=True)
    multialgos = models.IntegerField()
    lastblock = models.CharField(max_length=128, blank=True, null=True)
    network_ttf = models.IntegerField(blank=True, null=True)
    actual_ttf = models.IntegerField(blank=True, null=True)
    pool_ttf = models.IntegerField(blank=True, null=True)
    last_network_found = models.IntegerField(blank=True, null=True)
    installed = models.IntegerField(blank=True, null=True)
    watch = models.IntegerField()
    link_site = models.CharField(max_length=1024, blank=True, null=True)
    link_exchange = models.CharField(max_length=1024, blank=True, null=True)
    link_bitcointalk = models.CharField(max_length=1024, blank=True, null=True)
    link_github = models.CharField(max_length=1024, blank=True, null=True)
    link_explorer = models.CharField(max_length=1024, blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coins'


class Connections(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=64, blank=True, null=True)
    host = models.CharField(max_length=64, blank=True, null=True)
    db = models.CharField(max_length=64, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    idle = models.IntegerField(blank=True, null=True)
    last = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connections'


class Earnings(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    coinid = models.IntegerField(blank=True, null=True)
    blockid = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    mature_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earnings'
        unique_together = (('userid', 'blockid'),)


class Exchange(models.Model):
    coinid = models.IntegerField(blank=True, null=True)
    send_time = models.IntegerField(blank=True, null=True)
    receive_time = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_estimate = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    market = models.CharField(max_length=16, blank=True, null=True)
    tx = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exchange'


class Hashrate(models.Model):
    time = models.IntegerField(blank=True, null=True)
    hashrate = models.BigIntegerField(blank=True, null=True)
    hashrate_bad = models.BigIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rent = models.FloatField(blank=True, null=True)
    earnings = models.FloatField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashrate'


class Hashrenter(models.Model):
    renterid = models.IntegerField(blank=True, null=True)
    jobid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    hashrate = models.FloatField(blank=True, null=True)
    hashrate_bad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashrenter'


class Hashstats(models.Model):
    time = models.IntegerField(blank=True, null=True)
    hashrate = models.BigIntegerField(blank=True, null=True)
    earnings = models.FloatField(blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashstats'


class Hashuser(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    hashrate = models.BigIntegerField(blank=True, null=True)
    hashrate_bad = models.BigIntegerField(blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hashuser'


class Jobs(models.Model):
    renterid = models.IntegerField(blank=True, null=True)
    ready = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)
    host = models.CharField(max_length=1024, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=1024, blank=True, null=True)
    password = models.CharField(max_length=1024, blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Jobsubmits(models.Model):
    jobid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobsubmits'


class MarketHistory(models.Model):
    time = models.IntegerField()
    idcoin = models.ForeignKey(Coins, models.DO_NOTHING, db_column='idcoin')
    price = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    idmarket = models.ForeignKey('Markets', models.DO_NOTHING, db_column='idmarket', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_history'


class Markets(models.Model):
    coinid = models.IntegerField(blank=True, null=True)
    disabled = models.IntegerField()
    marketid = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    lastsent = models.IntegerField(blank=True, null=True)
    lasttraded = models.IntegerField(blank=True, null=True)
    balancetime = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    txfee = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    ontrade = models.FloatField()
    price = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    pricetime = models.IntegerField(blank=True, null=True)
    deposit_address = models.CharField(max_length=1024, blank=True, null=True)
    message = models.CharField(max_length=2048, blank=True, null=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    base_coin = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markets'


class Mining(models.Model):
    usdbtc = models.FloatField(blank=True, null=True)
    last_monitor_exchange = models.IntegerField(blank=True, null=True)
    last_update_price = models.IntegerField(blank=True, null=True)
    last_payout = models.IntegerField(blank=True, null=True)
    stratumids = models.CharField(max_length=1024, blank=True, null=True)
    best_algo = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mining'


class Nicehash(models.Model):
    active = models.IntegerField(blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    last_decrease = models.IntegerField(blank=True, null=True)
    algo = models.CharField(max_length=32, blank=True, null=True)
    btc = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    workers = models.IntegerField(blank=True, null=True)
    accepted = models.FloatField(blank=True, null=True)
    rejected = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nicehash'


class Notifications(models.Model):
    idcoin = models.ForeignKey(Coins, models.DO_NOTHING, db_column='idcoin')
    enabled = models.IntegerField()
    description = models.CharField(max_length=128, blank=True, null=True)
    conditiontype = models.CharField(max_length=32, blank=True, null=True)
    conditionvalue = models.FloatField(blank=True, null=True)
    notifytype = models.CharField(max_length=32, blank=True, null=True)
    notifycmd = models.CharField(max_length=512, blank=True, null=True)
    lastchecked = models.PositiveIntegerField(blank=True, null=True)
    lasttriggered = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Orders(models.Model):
    coinid = models.IntegerField(blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    ask = models.FloatField(blank=True, null=True)
    bid = models.FloatField(blank=True, null=True)
    market = models.CharField(max_length=16, blank=True, null=True)
    uuid = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Payouts(models.Model):
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    idcoin = models.ForeignKey(Coins, models.DO_NOTHING, db_column='idcoin', blank=True, null=True)
    time = models.IntegerField()
    completed = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    tx = models.CharField(max_length=128, blank=True, null=True)
    memoid = models.CharField(max_length=128, blank=True, null=True)
    errmsg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payouts'


class Rawcoins(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    symbol = models.CharField(max_length=32, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawcoins'


class Renters(models.Model):
    created = models.IntegerField(blank=True, null=True)
    updated = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    apikey = models.CharField(max_length=1024, blank=True, null=True)
    received = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    unconfirmed = models.FloatField(blank=True, null=True)
    spent = models.FloatField(blank=True, null=True)
    custom_start = models.FloatField(blank=True, null=True)
    custom_balance = models.FloatField(blank=True, null=True)
    custom_accept = models.FloatField(blank=True, null=True)
    custom_reject = models.FloatField(blank=True, null=True)
    custom_address = models.CharField(max_length=1024, blank=True, null=True)
    custom_server = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'renters'


class Rentertxs(models.Model):
    renterid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    tx = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rentertxs'


class Servers(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    maxcoins = models.IntegerField(blank=True, null=True)
    uptime = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servers'


class Services(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    algo = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    speed = models.BigIntegerField(blank=True, null=True)
    custom_balance = models.FloatField(blank=True, null=True)
    custom_accept = models.FloatField(blank=True, null=True)
    custom_reject = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Settings(models.Model):
    param = models.CharField(primary_key=True, max_length=128)
    value = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class Shares(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    workerid = models.IntegerField(blank=True, null=True)
    coinid = models.IntegerField(blank=True, null=True)
    jobid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    extranonce1 = models.IntegerField(blank=True, null=True)
    difficulty = models.FloatField()
    share_diff = models.FloatField()
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shares'


class Stats(models.Model):
    time = models.IntegerField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    wallet = models.FloatField(blank=True, null=True)
    wallets = models.FloatField(blank=True, null=True)
    immature = models.FloatField(blank=True, null=True)
    margin = models.FloatField(blank=True, null=True)
    waiting = models.FloatField(blank=True, null=True)
    balances = models.FloatField(blank=True, null=True)
    onsell = models.FloatField(blank=True, null=True)
    renters = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class Stratums(models.Model):
    pid = models.IntegerField(primary_key=True)
    time = models.IntegerField(blank=True, null=True)
    started = models.PositiveIntegerField(blank=True, null=True)
    algo = models.CharField(max_length=64, blank=True, null=True)
    workers = models.PositiveIntegerField()
    port = models.PositiveIntegerField(blank=True, null=True)
    symbol = models.CharField(max_length=16, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)
    fds = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'stratums'


class Withdraws(models.Model):
    market = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'withdraws'


class Workers(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    subscribe = models.IntegerField(blank=True, null=True)
    difficulty = models.FloatField(blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    dns = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    nonce1 = models.CharField(max_length=64, blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    worker = models.CharField(max_length=64, blank=True, null=True)
    algo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers'
